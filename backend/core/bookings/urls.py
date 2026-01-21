from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health),
    path('bookings/', views.list_bookings),
    path('bookings/create/', views.create_booking),
    path('bookings/<int:booking_id>/assign/', views.assign_provider),
    path('bookings/<int:booking_id>/status/', views.update_status),
    path('bookings/<int:booking_id>/events/', views.booking_events),
]
