from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rightmovecargo.rmcapi.models import LocalSession, User, UserCompany
from rightmovecargo.rmcapi.serializers import UserCompanySerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class UserCompanyViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer;
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
        type_code = request.GET.get('user_type', None);
        user = self.get_user(request);
        if user==None:
            return self.onError(request.data,"Invalid session",status.HTTP_400_BAD_REQUEST);

        if type_code == None:
            queryset = self.get_queryset().filter(user=user)
        else:
            queryset = self.get_queryset().filter(company=self.get_company(request),user_type__type_code=type_code)

        serializer = self.get_serializer(queryset, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);
