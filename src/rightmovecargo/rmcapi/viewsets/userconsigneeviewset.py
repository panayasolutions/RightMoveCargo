from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rightmovecargo.rmcapi.models import LocalSession, User, UserCompany, UserConsignee
from rightmovecargo.rmcapi.serializers import UserCompanySerializer, UserConsigneeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class UserConsigneeViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserConsignee.objects.all()
    serializer_class = UserConsigneeSerializer;
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
        # LocalSession.objects.all().delete();
        user_id = request.GET.get('user', None)

        if user_id == None:
            queryset = self.get_queryset().filter(company=self.get_company(request))
        else:
            queryset = self.get_queryset().filter(company=self.get_company(request),user__userid=user_id)

        serializer = self.get_serializer(queryset, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
