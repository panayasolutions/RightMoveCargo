
from rest_framework import status
from rest_framework.response import Response
from rightmovecargo.rmcapi.models import Courier, LocalSession, User, PinCode,Destination
from rightmovecargo.rmcapi.serializers import PinCodeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.thirdpartyapi.api import API;
from django.db import connection
from django.core import serializers


class PinCodeViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PinCode.objects.all()
    serializer_class = PinCodeSerializer;
    api = API
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
        print("PincodeViewSet.py ,list : ");
        user = self.get_user(request);
        pincode = request.GET.get('pincode', None);
        courier = request.GET.get('courier', None);
        shipment = request.GET.get('shipment', None);
        page = request.GET.get('page', None);
        active = 'YES';
        
        query = 'SELECT pc.PinCode as PinCode,pc.BranchCode as branchcode ,pc.ODA as oda,pc.ToPayorCod as topaycod,pc.CourierCode as CourierCode,pc.CompanyCode as compnaycode,pc.PickUp as pickup'
        query = query+' ,dest.destinationcode,dest.destinationname,dest.statecode'
        query = query+' FROM mtPin as pc inner join mtDestination as dest on pc.pincode=dest.destinationcode'
        query = query+' WHERE pc.Active=%s'
        params = [active];
        result = any;
        pincodes = self.api.get_pin_code(self.api,courier,[pincode]);
        pincodeser = self.get_serializer(pincodes,many=True);

        queryset = self.get_queryset();
        if courier != None:
            queryset =  self.get_queryset().filter(courier=courier)
            if pincode != None:
                queryset =  self.get_queryset().filter(courier=courier,pincode=pincode)
                # queryset = self.get_queryset().filter(pincode=pincode)

        page = self.paginate_queryset(queryset);
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:
           serializer = self.get_serializer(queryset, many=True) 

        pincodes = serializer.data+pincodeser.data        
        return self.onSuccess(pincodes," ",status.HTTP_200_OK)

    def dictfetchall(self, cursor):
        """Returns all rows from a cursor as a dict"""
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()]