from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status
from rightmovecargo.rmcapi.models import RateCalculator
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.serializers import  RateCalculatorSerializer

class RateCalculatorViewSet(BaseViewSet):
    
    """
    create user,
    update user
    login
    logout
    fetch current user info
    
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RateCalculator.objects.all()
    serializer_class = RateCalculatorSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # queryset = None
        pincode = request.GET.get('pincode', None);
        doctype = request.GET.get('doctype', None);
        weight = request.GET.get('weight', None);
        mode = request.GET.get('mode', None);
        client = request.GET.get('client', None);
        riskcover = request.GET.get('riskcover', None);
        codamt = request.GET.get('codamt', None);
        amount = request.GET.get('amount', None);
        print("pincode="+pincode+"&doctype="+doctype+"&weight="+weight+"&mode="+mode+"&client="+client+"&riskcover="+riskcover+"&codamt="+codamt+"&amount="+amount+"")

        # if self.get_user_type(request).type_code != 'ZCLN':
        #     queryset = self.get_queryset().filter(company=self.get_company(request).company_code)
        # else:
        #     queryset = self.get_queryset().filter(
        #         company=self.get_company(request).company_code,
        #         userid = self.get_user(request).userid)


        # serializer = self.get_serializer(queryset,many=True) 
        return self.onSuccess(self.test_date()," ",status.HTTP_200_OK);


    def test_date(self):
        date = [
            {"Freight": "0.00", "Risk": "0.00", "ODA": "0.00", "topaycod": "0.00", "awb": "0.00", "fuel": "0.00", "other": "0.00", "adjustment": "0.00", "gst": "0.00", "total": "0.00", "couriername": "DELHIVERY CARGO", "pinservice": "YES"}, 
            {"Freight": "0.00", "Risk": "0.00", "ODA": "0.00", "topaycod": "0.00", "awb": "0.00", "fuel": "0.00", "other": "0.00", "adjustment": "0.00", "gst": "0.00", "total": "0.00", "couriername": "DELHIVERY COURIER", "pinservice": "YES"},
             {"Freight": "0.00", "Risk": "0.00", "ODA": "0.00", "topaycod": "0.00", "awb": "0.00", "fuel": "0.00", "other": "0.00", "adjustment": "0.00", "gst": "0.00", "total": "0.00", "couriername": "DTDC COURIER", "pinservice": "YES"}, 
             {"Freight": "0.00", "Risk": "0.00", "ODA": "0.00", "topaycod": "0.00", "awb": "0.00", "fuel": "0.00", "other": "0.00", "adjustment": "0.00", "gst": "0.00", "total": "0.00", "couriername": "PROFESSIONAL COURIER", "pinservice": "YES"}, 
             {"Freight": "60.00", "Risk": "0.00", "ODA": "0.00", "topaycod": "0.00", "awb": "0.00", "fuel": "0.00", "other": "0.00", "adjustment": "0.00", "gst": "10.80", "total": "70.80", "couriername": "TRACKON COURIER", "pinservice": "YES"}]
        return date;
        