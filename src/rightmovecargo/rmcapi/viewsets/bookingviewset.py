from datetime import datetime
from rest_framework import viewsets
from rest_framework import permissions
from django.db import IntegrityError
from rest_framework import status
from rightmovecargo.rmcapi.models import BookingWeb, Client, Company, Consignee, Courier, CourierShipmentMode, ShipmentMode, ChildBooking, User, UserCompany, UserType
from rightmovecargo.rmcapi.thirdpartyapi.api import API
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
    api = API();
    # permission_classes = [permissions.IsAuthenticated]      

    def create(self, request, *args, **kwargs):
        if(request.data['awbType'] == 'A'):
            courier = request.data['courier']
            noPieces = request.data["prodPiece"]
            prodMod = request.data["prodMod"]
            prodIty = request.data["prodIty"]
            prodWeight = request.data["prodWeight"]
            pin = request.data["consignee"]['pin']
            eway_nos = self.api.get_fetch_eway_code(courier,[noPieces],pin,prodIty,prodWeight,prodMod);
            request.data['awbNo'] = eway_nos
            print(eway_nos);
        
        bookingJSON = json.dumps(request.data);
        with connection.cursor() as cursor:
         if courier=='DELC':
            cursor.execute("{call sp_insert_booking_delhivery('"+bookingJSON+"')}")
         else:
            cursor.execute("{call sp_insert_booking('"+bookingJSON+"')}") 
            request.data['awbNo']=cursor.fetchone()[0];  
            print(request.data['awbNo']);
        if request.data['awbNo'] is None or request.data['awbNo'] == '':
            return self.onError(request.data,"Something went wrong",status.HTTP_400_BAD_REQUEST);
            serializer = self.get_serializer(data=request.data)
        print(request.data)
        booking =BookingWeb.objects.get(awbNo=request.data['awbNo']);
        createLabel(booking);
        # createDocket(booking);
        createReceipt(booking);
        # booking =BookingWeb.objects.get(awbNo='500188521842');
        # createReceipt(booking);
        return  self.onSuccess([request.data],"Record created successfully",status.HTTP_201_CREATED);

    def update(self, request, *args, **kwargs):
        #print(json.dumps(request.data))
        with connection.cursor() as cursor:
            cursor.execute("{call sp_Inscan_booking('"+json.dumps(request.data)+"')}")
            print(request.data['awbNo']);
        cursor.close();
        
        if request.data['awbNo'] is None or request.data['awbNo'] == '':
            return self.onError([request.data],"Something went wrong",status.HTTP_400_BAD_REQUEST);
        
        booking =BookingWeb.objects.get(awbNo=request.data['awbNo']);
        apiResponse = self.api.create_booking(booking);

        if apiResponse is not None and apiResponse != '':
            return self.onError([request.data],apiResponse,status.HTTP_400_BAD_REQUEST);
        

        # serializer = self.get_serializer(data=request.data)
        #print(serializer.is_valid(raise_exception=True))
            # if serializer.is_valid():
        # cursor.close();
        
        # self.api.test();
        # createDocket(booking);
        return  self.onSuccess([request.data],"Record updated successfully",status.HTTP_201_CREATED);

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
                booking.shipment = ShipmentMode.objects.get(shipment_mode_code=booking.shipment);
                booking.shipment.shipment_courier = None #Courier.objects.get(branchcode=booking.courier.branchcode);
                # booking.courier.courier_shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                # booking.shipment = ShipmentMode.objects.filter(shipment_mode_code='CA')
                booking.dim = ChildBooking.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except ChildBooking.DoesNotExist :
                booking.dim = None
        page = self.paginate_queryset(queryset);
        if page is not None:
            serializer = self.get_serializer(page, many=True) 
        else:
           serializer = self.get_serializer(queryset, many=True) 
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK)
        
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
                booking.shipment = ShipmentMode.objects.get(shipment_mode_code=booking.shipment)
                booking.shipment.shipment_courier = Courier.objects.filter(
                companycouriermode__couriershipmentmode__shipment_mode=booking.shipment,
                companycouriermode__company=company_code,
                companycouriermode__user_type=user_type,
                companycouriermode__courier=booking.courier,
                )
                booking.dim = ChildBooking.objects.filter(masterawbno=booking.awbNo)
            except Consignee.DoesNotExist :
                booking.consignee = None
            except ShipmentMode.DoesNotExist :
                booking.shipment = None
            except ChildBooking.DoesNotExist :
                booking.dim = None
                
        serializer = self.get_serializer(queryset , many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);