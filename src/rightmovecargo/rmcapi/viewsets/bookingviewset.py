from rest_framework import viewsets
from rest_framework import permissions
from django.db import IntegrityError
from rest_framework import status
from rightmovecargo.rmcapi.models import BookingWeb, Client, Company, Consignee, Courier, CourierShipmentMode, ShipmentMode, Tbbookingchild, User, UserCompany, UserType
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.serializers import BookingSerializer, UserSerializer
from django.db import connection
import json
from rest_framework.decorators import api_view
class BookingViewSet(BaseViewSet):
    
   
    queryset = BookingWeb.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]      

    def create(self, request, *args, **kwargs):
            with connection.cursor() as cursor:
                cursor.execute("{call sp_insert_booking('"+json.dumps(request.data)+"')}")
                request.data['awbNo']=cursor.fetchone()[0];
                
            return  self.onSuccess([request.data],"Record created successfully",status.HTTP_201_CREATED);

   
    def list(self, request, *args, **kwargs):
        queryset = None
        user = self.get_user(request);
        user_type = self.get_user_type(request).type_code;
        company_code = self.get_company(request).company_code;
        if user_type !='ZEMP':
            queryset = self.get_queryset().filter(user=user.userid)
        else:
            queryset = self.get_queryset().filter(companyCode=company_code)

        for booking in queryset:
            booking.client = Client.objects.get(userid=booking.user)
            try:
                booking.consignee = Consignee.objects.get(conscode=booking.consignee)
                booking.courier = Courier.objects.get(branchcode=booking.courier)
                booking.courier.courier_shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                # booking.shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                booking.dim = Tbbookingchild.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except Tbbookingchild.DoesNotExist :
                booking.dim = None
        serializer = self.get_serializer(queryset , many=True) # self.get_serializer(request.user)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    def retrieve(self, request, *args, **kwargs):
        awbNo = kwargs.get('pk');
        queryset = None
        user = self.get_user(request);
        user_type = self.get_user_type(request).type_code;
        company_code = self.get_company(request).company_code;
        if user_type !='ZEMP':
            queryset = self.get_queryset().filter(user=user.userid,awbNo=awbNo)
        else:
            queryset = self.get_queryset().filter(companyCode=company_code,awbNo=awbNo)

        for booking in queryset:
            booking.client = Client.objects.get(userid=booking.user)
            try:
                booking.consignee = Consignee.objects.get(conscode=booking.consignee)
                booking.courier = Courier.objects.get(branchcode=booking.courier)
                booking.courier.courier_shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                booking.dim = Tbbookingchild.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except Tbbookingchild.DoesNotExist :
                booking.dim = None
        serializer = self.get_serializer(queryset , many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
        