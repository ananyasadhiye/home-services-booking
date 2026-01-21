from django.contrib import admin
from bookings.views import home
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),
]
