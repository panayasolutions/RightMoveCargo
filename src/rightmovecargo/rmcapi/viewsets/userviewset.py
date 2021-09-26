from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status
from rightmovecargo.rmcapi.models import Company, User, UserCompany, UserType
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rightmovecargo.rmcapi.serializers import UserSerializer

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
    # permission_classes = [permissions.IsAuthenticated]

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
        queryset = None
        utype = request.GET.get('utype', None);
        if utype != None:
            queryset = self.get_queryset().filter(user__company=self.get_company(request),user__user_type=utype)
        else:
            queryset = self.get_queryset().filter(user__company=self.get_company(request))
            
        serializer = self.get_serializer(queryset,many=True) 
        # user = self.get_user(request);
        # if user==None:
        #     return self.onError(request.data,"Invalid session",status.HTTP_400_BAD_REQUEST);
        
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    def retrieve(self, request, *args, **kwargs):
        user = self.get_user(request);
        if user==None:
            return self.onError(request.data,"Invalid session",status.HTTP_400_BAD_REQUEST);
        serializer = self.get_serializer(user)
        return self.onSuccess([serializer.data]," ",status.HTTP_200_OK);
        # queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
       
    #     user = self.get_user(request);
    #     # qCompnay = self.filter_queryset(self.get_queryset().filter(
    #     #      usercompany__user = user
    #     #     ));
        
    #     # serializer = self.get_serializer(user)
        
    #     # qCompnay = User.objects.all().filter(company__user=user);
    #     print(qCompnay.query);
    #     serializer = self.get_serializer(qCompnay,many=False)
        
    #     return self.onSuccess(serializer.data,"Record created successfully",status.HTTP_201_CREATED);
        return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)
  
# #  resolve keyword 'user' into field. Choices are: branch, company, editby, editdatetime, emailid, enterby, 
# # entrydatetime, invalidcount, is_active, iv, password, resettimestamp, resettoken, usercompany, userconsignee, 
# # userid, username, userrights, usertype
        