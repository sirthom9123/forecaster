from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('save_forecast', views.save_forecast, name='save_forecast'),
    path('history_data/', views.history_data, name='history_data'),
    path('search_data', csrf_exempt(views.search_data), name='search_data'),
    path('export_csv', views.export_csv, name='export_csv'),
]
