from datetime import datetime
from rest_framework import viewsets
from rest_framework import permissions
from django.db import IntegrityError
from rest_framework import status
from rightmovecargo.rmcapi.models import BookingWeb, Client, Company, Consignee, Courier, CourierShipmentMode, ShipmentMode, ChildBooking, User, UserCompany, UserType
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.serializers import BookingSerializer, UserSerializer
from django.db import connection
import json
from rest_framework.decorators import api_view
from rightmovecargo.rmcapi.docutil.docketutil import createDocket
from rightmovecargo.rmcapi.docutil.labelutil import createLabel
from rightmovecargo.rmcapi.docutil.receiptutil import createReceipt; #receipt
# from rightmovecargo.rmcapi.docutil.invoiceutil import createInvoice;
# createInvoice('');
class BookingViewSet(BaseViewSet):
    
   
    queryset = BookingWeb.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]      

    def create(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("{call sp_insert_booking('"+json.dumps(request.data)+"')}")
            request.data['awbNo']=cursor.fetchone()[0];  
            print(request.data['awbNo']);
            if request.data['awbNo'] is None or request.data['awbNo'] == '':
                return self.onError(request.data,"Something went wrong",status.HTTP_400_BAD_REQUEST);
            serializer = self.get_serializer(data=request.data)
            # print(serializer.is_valid(raise_exception=True))
        #if serializer.is_valid():
            booking =BookingWeb.objects.get(awbNo=request.data['awbNo']);
            createLabel(booking);
            # createDocket(booking);
            createReceipt(booking);
        # booking =BookingWeb.objects.get(awbNo='500188521842');
        # createReceipt(booking);
        return  self.onSuccess([request.data],"Record created successfully",status.HTTP_201_CREATED);

    def update(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("{call sp_update_booking('"+json.dumps(request.data)+"')}")
            request.data['awbNo']=cursor.fetchone()[0];  
            print(request.data['awbNo']);
            if request.data['awbNo'] is None or request.data['awbNo'] == '':
                return self.onError([request.data],"Something went wrong",status.HTTP_400_BAD_REQUEST);
            # serializer = self.get_serializer(data=request.data)
            #print(serializer.is_valid(raise_exception=True))
            # if serializer.is_valid():
            booking =BookingWeb.objects.get(awbNo=request.data['awbNo']);
            createDocket(booking);
        return  self.onSuccess([request.data],"Record created successfully",status.HTTP_201_CREATED);

    def list(self, request, *args, **kwargs):
        queryset = None
        user = self.get_user(request);
        user_type = self.get_user_type(request).type_code;
        company_code = self.get_company(request).company_code;
        if user_type !='ZEMP':
            queryset = self.filter_queryset(self.get_queryset()).filter(user=user.userid).order_by('awbNo')
        else:
            queryset = self.filter_queryset(self.get_queryset()).filter(companyCode=company_code).order_by('awbNo')
       # page = self.paginate_queryset(queryset)
        for booking in queryset:
            booking.client = Client.objects.get(userid=booking.user)
            try:
                booking.consignee = Consignee.objects.get(conscode=booking.consignee)
                booking.courier = Courier.objects.get(branchcode=booking.courier)
                booking.courier.courier_shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                # booking.shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                booking.dim = ChildBooking.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except ChildBooking.DoesNotExist :
                booking.dim = None
        # if page is not None:
        #     serializer = self.get_pagination_serializer(page)
        # else:
        #     serializer = self.get_serializer(queryset, many=True)

        serializer = self.get_serializer(queryset , many=True) # self.get_serializer(request.user)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

        # queryset = self.queryset
        # parameters = self.get_request_params(self.request)
        # if 'ordering' in parameters:
        #     queryset = queryset.order_by(parameters['ordering'])
        #     del parameters['ordering']
        # queryset = queryset.filter(**parameters).distinct()
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # serializer = self.get_serializer(queryset, many=True)

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
                booking.dim = ChildBooking.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except ChildBooking.DoesNotExist :
                booking.dim = None
        serializer = self.get_serializer(queryset , many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
        