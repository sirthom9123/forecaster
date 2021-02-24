from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
import requests
import json
import os 
import csv
import datetime
 
from .models import City
from .forms import LocationForm


@login_required(login_url='/authentication/login')
def index(request):
    key = settings.WEATHER_API
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,alerts&mode=json&units=metric&appid=' + key + ''
    form = LocationForm()
    
    
    if request.method == "POST":
        form = LocationForm(request.POST or None)    
        
        if form.is_valid():  
            text = form.cleaned_data['location'].split(',')
            lat = text[1]
            lon = text[0]
            
            data = requests.get(url.format(lat, lon)).json()
            
            forecast_data = {
                'lat': lat,
                'lon': lon,
                'temperature': data['current']['temp'],
                'humidity': data['current']['humidity'],
                'wind': data['current']['wind_speed'],
                'description': data['current']['weather'][0]['description'],
                'icon': data['current']['weather'][0]['icon'],
                'hourly': data['hourly'][0]['temp'],
            }
            
            with open('data.json', 'w') as f:
                json.dump(forecast_data, f)
            
        context = {'forecast': forecast_data}
        return render(request, 'index.html', context)
    
        
    context = {'form': form}
    return render(request, 'index.html', context)




@login_required(login_url='/authentication/login')
def save_forecast(request):    
    file_path = os.path.join(settings.BASE_DIR, 'data.json')
    with open(file_path, 'r') as json_file:
        data =  json.load(json_file)
             
        forecast = City.objects.create(owner=request.user,
            lat=data['lat'], 
            lon=data['lon'], 
            temperature=data['temperature'],
            humidity=data['humidity'],
            wind=data['wind'],
            description=data['description'],
        )        
        messages.success(request, 'Weather data saved succesfully')
        return redirect('/')
    
    
@login_required(login_url='/authentication/login')
def history_data(request):
    cities = City.objects.filter(owner=request.user)
    paginator = Paginator(cities, 6)
    page = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page)
    return render(request, 'history.html', {'cities': cities, 'page_obj': page_obj})


def search_data(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        cities = City.objects.filter(
            lat__istartswith=search_str, owner=request.user) | City.objects.filter(
            lon__istartswith=search_str, owner=request.user) | City.objects.filter(
            temperature__istartswith=search_str, owner=request.user) | City.objects.filter(
            humidity__istartswith=search_str, owner=request.user) | City.objects.filter(
            wind__istartswith=search_str, owner=request.user) | City.objects.filter(
            description__icontains=search_str, owner=request.user) | City.objects.filter(
            created__icontains=search_str, owner=request.user)
        data = cities.values()
        
        return JsonResponse(list(data), safe=False)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Income'+str(datetime.datetime.now())+'.csv'
    
    writer= csv.writer(response)
    writer.writerow(['Amount', 'Description', 'Source', 'Date'])
    
    city = City.objects.filter(owner=request.user)
    
    for location in city:
        writer.writerow([location.lat, location.lon, location.temperature, location.humidity, location.wind, location.description, location.created])
        
    return response