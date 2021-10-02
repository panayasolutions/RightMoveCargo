from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.rmcapi.models import Attachment, Company, UserType
from rest_framework import status
from rightmovecargo.rmcapi.serializers import AttachmentSerializer, CompanySerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser
import os

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
            up_file = request.FILES['declarationdata'];
            serializer.validated_data["declarationdata"] = up_file.file.read();
            serializer.validated_data["dfilename"] = up_file.name;
            serializer.validated_data["deextn"] = self.extension(up_file.name);
            print(up_file.file);
            # print(request.data)
            # serializer.perform_create();
            serializer.save()
        #     print(request.POST.get('declarationdata',False))
        #     # serializer.validated_data['user_type_code'] = self.create_id('USER','TYPE');
        #     # serializer.validated_data['modified_by'] = request.user;
        #     # serializer.validated_data['created_by'] = request.user;
        #     self.perform_create(serializer)
            return  self.onSuccess("",up_file.name+" File with "+request.data["awbno"]+" uploaded successfully",status.HTTP_201_CREATED);
        return  self.onError([""],serializer._errors,status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):

    #     # qCompnay = self.filter_queryset(self.get_queryset().filter(
    #     #     company_courier__user_type= self.get_user_type(request)
            
    #     # ));
    #     # print(que ryset.query)
    #     # print(qCompnay.query);
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    def retrieve(self, request, *args, **kwargs):
        awbNo = kwargs.get('pk');
        serializer = self.get_serializer(self.get_queryset().filter(awbno=awbNo), many=True)
        return self.onSuccess(serializer.data," ",status.HTTP_200_OK);

    def extension(self,filename):
        name, extension = os.path.splitext(filename)
        return extension
    

