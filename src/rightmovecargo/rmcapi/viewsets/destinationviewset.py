from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rightmovecargo.rmcapi.models import LocalSession, User, PinCode,Destination
from rightmovecargo.rmcapi.serializers import DestinationSerializer, PinCodeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class DestinationViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer;
    # permission_classes = [permissions.IsAuthenticated]
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid(raise_exception=False):
    #         serializer.validated_data['user_type_code'] = self.create_id('USER','TYPE');
    #         # serializer.validated_data['modified_by'] = request.user;
    #         # serializer.validated_data['created_by'] = request.user;
    #         self.perform_create(serializer)
    #         return  self.onSuccess([serializer.data],"Record created successfully",status.HTTP_201_CREATED);
    #     return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)

# Branch by User 
# User By Branch (filter type=user_type)
    def list(self, request, *args, **kwargs):
        user = self.get_user(request);
        pincode = request.GET.get('pincode', None);
        courier = request.GET.get('courier', None);
        shipment = request.GET.get('shipment', None);
        if pincode == None:
            queryset = self.get_queryset()
        else:
            queryset = self.get_queryset().filter(destinationcode=pincode)
        serializer = self.get_serializer(queryset, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
