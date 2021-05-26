import re
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rightmovecargo.rmcapi.models import Consignee
from rightmovecargo.rmcapi.serializers import ConsigneeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class ConsigneeViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Consignee.objects.all()
    serializer_class = ConsigneeSerializer;

    def list(self, request, *args, **kwargs):
        queryset = None;
        client = request.GET.get('client', None);
        if client!=None:
            queryset = self.get_queryset().filter(
                userconsignee__company=self.get_company(request),
                userconsignee__user = client
            )
        else:
            queryset = self.get_queryset().filter(
                userconsignee__company=self.get_company(request)
            )
        serializer = self.get_serializer(queryset, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
