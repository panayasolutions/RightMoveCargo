from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import Company, UserType
from rest_framework import status
from rightmovecargo.rmcapi.serializers import CompanySerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class CompanyViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer;
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

        qCompnay = self.filter_queryset(self.get_queryset().filter(
            company_courier__user_type= self.get_user_type(request)
            
        ));
        # print(que ryset.query)
        # print(qCompnay.query);
        serializer = self.get_serializer(qCompnay, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    

