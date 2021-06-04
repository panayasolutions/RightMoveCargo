from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import Courier, CourierShipmentMode, ShipmentMode
from rest_framework import status
from rightmovecargo.rmcapi.serializers import CourierSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class CourierViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer;
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

    def list(self, request, *args, **kwargs):
        user_type = self.get_user_type(request);
        company = self.get_company(request);
        qCouriers = Courier.objects.filter(
            companycouriermode__company=company,
            companycouriermode__user_type=user_type
            )
        for courier in qCouriers:
            for company_courier in courier.companycouriermode_set.filter(user_type=user_type,company=company):
                #print(company_courier.company_courier_mode_code+"==="+company_courier.company.company_code+" ===== "+courier.branchcode+"====="+company_courier.user_type.type_code)
                #courier.courier_shipment = CourierShipmentMode.objects.filter(company_courier=meme)
                courier.courier_shipment = ShipmentMode.objects.filter(
                    couriershipmentmode__company_courier = company_courier
                )
        serializer = self.get_serializer(qCouriers,many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

