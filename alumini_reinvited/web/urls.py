from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name='home_view'),  
    path('profile/',views.profile_view, name='profile_view'),
    path('connections/',views.connections_view, name='connections_view'),
    path('events/',views.events_view, name='events'),
    
]