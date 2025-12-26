from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sample_api(request):
    return Response({"message": "Hello from the Listings App!"})

class ListingViewSet(viewsets.ModelViewSet):
    """ Viewset for viewing and editing listings. """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """ Viewset for viewing and editing bookings"""

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer