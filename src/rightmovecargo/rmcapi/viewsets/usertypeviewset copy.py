from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import UserType
from rest_framework import status
from rightmovecargo.rmcapi.serializers import UserTypeSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet

class UserTypeViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer;
    # permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.validated_data['user_type_code'] = self.create_id('USER','TYPE');
            # serializer.validated_data['modified_by'] = request.user;
            # serializer.validated_data['created_by'] = request.user;
            self.perform_create(serializer)
            return  self.onSuccess([serializer.data],"Record created successfully",status.HTTP_201_CREATED);
        return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)

    

