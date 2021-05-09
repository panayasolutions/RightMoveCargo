from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from custauth.models import User
from custauth.serializers.userserializer import UserSerializer

class BaseViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        return self.onError("","POST method not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 
    
    def delete(self, request, *args, **kwargs):
        return self.onError("","DELETE not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def retrieve(self, request, *args, **kwargs):
        return self.onError("","GET not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def update(self, request, *args, **kwargs):
        return self.onError("","PUT not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 

    def list(self, request, *args, **kwargs):
        return self.onError("","GET LIST not allowed",status.HTTP_405_METHOD_NOT_ALLOWED) 
    
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
        

        