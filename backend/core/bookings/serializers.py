from rest_framework import serializers
from .models import Booking, Provider, BookingEvent

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingEvent
        fields = '__all__'
