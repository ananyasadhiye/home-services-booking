from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Booking, Provider, BookingEvent
from .serializers import BookingSerializer, ProviderSerializer, BookingEventSerializer

VALID_TRANSITIONS = {
    'PENDING': ['ASSIGNED', 'CANCELLED'],
    'ASSIGNED': ['IN_PROGRESS', 'REJECTED', 'CANCELLED'],
    'IN_PROGRESS': ['COMPLETED'],
}

def log_event(booking, old, new, actor):
    BookingEvent.objects.create(
        booking=booking,
        old_status=old,
        new_status=new,
        actor=actor
    )
def home(request):
    return JsonResponse({
        "status": "ok",
        "service": "Home Services Booking API",
        "version": "v1",
        "server_time": now().isoformat(),
        "description": "API for managing booking lifecycle, provider workflows, and observability",
        "available_endpoints": {
            "list_bookings": "GET /api/bookings/",
            "create_booking": "POST /api/bookings/create/",
            "assign_provider": "POST /api/bookings/<id>/assign/",
            "update_status": "POST /api/bookings/<id>/status/",
            "booking_events": "GET /api/bookings/<id>/events/"
        }
    })
def health(request):
    return JsonResponse({"status": "healthy"})
@api_view(['POST'])
def create_booking(request):
    booking = Booking.objects.create(
        customer_name=request.data['customer_name'],
        service_type=request.data['service_type']
    )
    return Response(BookingSerializer(booking).data)

@api_view(['GET'])
def list_bookings(request):
    return Response(BookingSerializer(Booking.objects.all(), many=True).data)

@api_view(['POST'])
def assign_provider(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    provider = Provider.objects.filter(available=True).first()

    if not provider:
        return Response({"error": "No providers available"}, status=400)

    old = booking.status
    booking.provider = provider
    booking.status = 'ASSIGNED'
    booking.save()
    log_event(booking, old, 'ASSIGNED', 'system')

    return Response(BookingSerializer(booking).data)

@api_view(['POST'])
def update_status(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    new_status = request.data['status']

    if new_status not in VALID_TRANSITIONS.get(booking.status, []):
        return Response({"error": "Invalid transition"}, status=400)

    old = booking.status
    booking.status = new_status
    booking.save()
    log_event(booking, old, new_status, request.data.get('actor', 'admin'))

    return Response(BookingSerializer(booking).data)

@api_view(['GET'])
def booking_events(request, booking_id):
    events = BookingEvent.objects.filter(booking_id=booking_id)
    return Response(BookingEventSerializer(events, many=True).data)
