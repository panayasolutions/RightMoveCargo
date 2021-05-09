from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from custauth.models import User
from custauth.viewsets.baseviewset import BaseViewSet
from custauth.serializers.userserializer import UserSerializer

class UserViewSet(BaseViewSet):
    
    """
    create user,
    update user
    login
    logout
    fetch current user info
    
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        isValid = serializer.is_valid();
        if isValid==False:
            return self.onError(request.data,serializer._errors,status.HTTP_400_BAD_REQUEST);
        if request.user != None:
            serializer.data['enterby'] = request.user.id
        User.objects.create_user(**request.data);
        return self.onSuccess([request.data],request.data['username']+" created successfully",status.HTTP_201_CREATED);

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        isValid = serializer.is_valid();
        if isValid==False:
            return self.onError(request.data,serializer._errors,status.HTTP_400_BAD_REQUEST);
        if request.user != None:
            serializer.data['enterby'] = request.user.id
        User.objects.create_user(**request.data);
        return self.onSuccess(request.data,request.data['username']+" created successfully",status.HTTP_200_OK);

    def list(self, request, *args, **kwargs):
        user = request.user;
        if user==None:
            return self.onError(request.data,"Invalid session",status.HTTP_400_BAD_REQUEST);
        serializer = self.get_serializer(request.user)
        return self.onSuccess([serializer.data]," ",status.HTTP_200_OK);
  

        