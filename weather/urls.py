from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('save_forecast', views.save_forecast, name='save_forecast'),
    path('history_data/', views.history_data, name='history_data'),
    path('search_data', views.search_data, name='search_data'),
    path('export_csv', views.export_csv, name='export_csv'),
]
