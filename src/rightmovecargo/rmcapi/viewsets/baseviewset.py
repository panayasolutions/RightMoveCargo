from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
import secrets
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from rightmovecargo.rmcapi.constants import constant

from rightmovecargo.rmcapi.models import User

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = []
    user = None
    branch = None
    user_type = None
    def create(self, request, *args, **kwargs):
        return self.onError("","POST method not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 
    
    def destroy(self, request, *args, **kwargs):
        return self.onError("","DELETE not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def retrieve(self, request, *args, **kwargs):
        return self.onError("","GET not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def update(self, request, *args, **kwargs):
       
        # return super(viewsets.ModelViewSet,self).update(request, *args, **kwargs)
        return self.onError("","PUT not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def partial_update(self, request, *args, **kwargs):
        # return super(viewsets.ModelViewSet,self).update(request, *args, **kwargs)
        return self.onError("","PATCH not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def list(self, request, *args, **kwargs):
        # print('asdfasdf111111');
        return super(viewsets.ModelViewSet,self).list(self, request, *args, **kwargs)
        # return self.onError("","GET LIST not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 
    
    def onSuccess(self,response_data,success_msg,success_code):
        custom_response = {
            'success_code': success_code,
            'success_msg':success_msg,
            'results':response_data};
        headers = self.get_success_headers(response_data)
        return Response(custom_response, status=status.HTTP_200_OK, headers=headers);

    def onError(self,request_data,response_data,error_code):
        custom_response = {
            'error_code': error_code,
            "error_title" : "Server Error",
            'error_msg':response_data,
            'results':[request_data]};
        headers = self.get_success_headers(response_data)
        return Response(custom_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=headers);

    def get_company(self,request):
        
        if self.branch == None:
            # user_branch = UserBranch.objects.get(request.session.user_branch)
            # print(request.session.user_branch)
            # branch = Branch.objects.get(request.session.user_branch.branch)
            # print(request.session.user_branch.branch)
            return request.session.user_company.company

    def get_user_type(self,request):
        return request.session.user_company.user_type

    def get_user(self,request):
        if self.user == None:
            return request.user
        return self.user;

    def user_credentials_validation(self,username,password):
        
        sysuser = User.objects.all().get(userid=username);
        
        # print(sysuser.password);
        # print(sysuser.iv);
        # aes2 = AES.new(str(constant.KEYVAL).encode("utf8"), AES.MODE_CBC, sysuser.iv.encode("utf8"))
        
        # dwpwd = unpad(aes2.decrypt(sysuser.password), constant.BLOCKSIZE)
        # decryptpwd = dwpwd.decode()
        
        
        # # AES.new('\xd0\x86\x90a\xd4\\\xad\xb6\xcc\x83&z@\x1e\xee\x1a', AES.MODE_CBC,"WUoZ/mDpJh130Bw78g0QnA==")
        # if decryptpwd == password:
        #     return sysuser;
        return sysuser

    def create_id(self,prefix,suffix=None):
        record_id = prefix
        record_id = record_id+"_"+timezone.now().strftime("%Y%m%d%H%M%S")
        if suffix != None:
            record_id = record_id+"_"+suffix
        return record_id
        

        