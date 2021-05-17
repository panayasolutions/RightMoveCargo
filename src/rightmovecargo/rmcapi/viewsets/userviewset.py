from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rightmovecargo.rmcapi.models import Company, User, UserCompany, UserType
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.serializers import UserSerializer
from rightmovecargo.rmcapi import serializers

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
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['modified_by'] = request.user;
            serializer.validated_data['created_by'] = request.user;
            user = User.objects.create_user(**serializer.validated_data);
            return  self.onSuccess([request.data],"Record created successfully",status.HTTP_201_CREATED);
        return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        print('asdfadf');
        kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # return super(viewsets.ModelViewSet,self).update(request, *args, **kwargs);
        isValid = serializer.is_valid(raise_exception=True);
        if isValid==False:
            return self.onError(request.data,serializer._errors,status.HTTP_400_BAD_REQUEST);
        if request.user != None:
            serializer.validated_data['modified_by'] = request.user
        branchs = serializer.initial_data.get('branchs')
        try:
            for branch in branchs:
                user_type = UserType.objects.get(pk=branch.get("user_type"))
                branch = Company.objects.get(pk=branch.get("company_code"))
                userBranch = UserCompany(user=instance, branch=branch,user_type=user_type)
                # userBranch.modified_by = request.user;
                # userBranch.created_by = request.user;
                userBranch.user_branch_code = self.create_id('USR','BRNC')
                userBranch.save();
        except (IntegrityError) as e:
                return self.onError(request.data,instance.username+" is already mapped with "+branch.branch_name+" as "+user_type.user_type_name,status.HTTP_400_BAD_REQUEST);
        serializer.update(instance,serializer.validated_data);
        
        return self.onSuccess([]," updated successfully",status.HTTP_200_OK);
    def partial_update(self, request, *args, **kwargs):
        return super(viewsets.ModelViewSet,self).partial_update(request, *args, **kwargs);

    def list(self, request, *args, **kwargs):
        user = self.get_user(request);
        if user==None:
            return self.onError(request.data,"Invalid session",status.HTTP_400_BAD_REQUEST);
        serializer = self.get_serializer(request.user)
        return self.onSuccess([serializer.data]," ",status.HTTP_200_OK);

    # def list(self, request, *args, **kwargs):
    #     type_code = request.GET.get('user_type', None)
    #     user_type = UserType.objects.get(type_code=type_code)
    #     queryset = self.get_queryset().filter(
    #         user_branch__user_type=user_type,
    #         user_branch__user=request.user)
    #     # queryset = self.filter_queryset(self.get_queryset().filter(branchs__user_type=user_type))
    #     # print(user_type);
    #     print(queryset.query);
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
        # serializer = self.get_serializer(queryset,data=request.data)
        # print(queryset.query);
        # if serializer.is_valid(raise_exception=False):
            # print(serializer.validated_data);
            # return Response(serializer.data)
            # return self.onSuccess([serializer.data],"Record created successfully",status.HTTP_201_CREATED);
        # return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)
  

        