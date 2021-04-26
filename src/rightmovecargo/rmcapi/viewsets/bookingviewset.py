from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rightmovecargo.rmcapi.models import Booking
from rightmovecargo.rmcapi.serializers.bookingserialize import BookingSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    