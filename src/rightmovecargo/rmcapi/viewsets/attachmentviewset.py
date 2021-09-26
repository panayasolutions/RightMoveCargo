from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import Attachment, Company, UserType
from rest_framework import status
from rightmovecargo.rmcapi.serializers import AttachmentSerializer, CompanySerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser

class AttachmentViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer;
    # parser_classes = [MultiPartParser]
    parser_classes = (MultiPartParser,FileUploadParser,FormParser,JSONParser)
    # permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            print(request.POST.get('declarationdata',False))
            # serializer.validated_data['user_type_code'] = self.create_id('USER','TYPE');
            # serializer.validated_data['modified_by'] = request.user;
            # serializer.validated_data['created_by'] = request.user;
            self.perform_create(serializer)
            return  self.onSuccess([serializer.data],"Record created successfully",status.HTTP_201_CREATED);
        return  self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     file_obj = request.POST.get('form1', False)
    #     file = request.POST.get('file', False)
    #     print(file_obj);
    #     print(file);
    #     print(kwargs);
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return self.onError([request.data],serializer._errors,status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):

        qCompnay = self.filter_queryset(self.get_queryset().filter(
            company_courier__user_type= self.get_user_type(request)
            
        ));
        # print(que ryset.query)
        # print(qCompnay.query);
        serializer = self.get_serializer(qCompnay, many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    

