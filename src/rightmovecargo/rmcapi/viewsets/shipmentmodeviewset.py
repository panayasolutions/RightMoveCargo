from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import Company, Courier, ShipmentMode
from rest_framework import status
from rightmovecargo.rmcapi.serializers import  ShipmentModeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class ShipmentModeViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ShipmentMode.objects.all()
    serializer_class = ShipmentModeSerializer;
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
        # qShipment = ShipmentMode.objects.filter(
        #     companycouriermode__company=company,
        #     companycouriermode__user_type=user_type
        #     )
        qShipment = self.get_queryset().order_by("shipment_seq");
        for shipment in qShipment:

            shipment.shipment_courier = Courier.objects.filter(
                companycouriermode__couriershipmentmode__shipment_mode=shipment,
                companycouriermode__company=company,
                companycouriermode__user_type=user_type
            );


            # for courier_shipment in shipment.couriershipmentmode_set.filter(shipment_mode=shipment,
            #                                                                 company_courier__company = company,
            #                                                                 company_courier__user_type=user_type):

            #     print(shipment.shipment_mode_code+"  "+courier_shipment.courier_shipment_code+" "+courier_shipment.company_courier.courier.branchcode);
            #     # companycouriermode_set.filter(user_type=user_type,company=company):
            #     # shipment.shipment_courier = Courier.objects.filter(
            #     #     user_type=user_type,
            #     #     company1=company,
            #     #     # companycouriermode_set = courier_shipment.company_courier_id
            #     # )
            #     shipment.shipment_courier = Courier.objects.filter(
            #         companycouriermode__couriershipmentmode=courier_shipment
            #     )
                # ,
                    # companycouriermode= courier_shipment.company_courier
        serializer = self.get_serializer(qShipment,many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
