from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#now import the views.py file into this code
from . import views
from .views import find_flights
# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)



urlpatterns=[
  path('api/', include(router.urls)),
  path('api/findflights/', views.find_flights),
  ]
