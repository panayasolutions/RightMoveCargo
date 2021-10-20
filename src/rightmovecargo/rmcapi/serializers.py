from rest_framework import serializers

from rightmovecargo.rmcapi.models import Attachment, BookingWeb, Client, Company, CompanyCourierMode,  Consignee, Courier, CourierShipmentMode, Destination, LocalSession, PinCode, ShipmentMode, ChildBooking, User, UserCompany, UserConsignee, UserType
from django.core.files.uploadedfile import InMemoryUploadedFile
class BaseSerializer(serializers.HyperlinkedModelSerializer):
    def test():
        pass

class UserCompanySerializer(BaseSerializer):
    user_code = serializers.ReadOnlyField(source='user.userid')
    username = serializers.ReadOnlyField(source='user.username')
    company_code = serializers.ReadOnlyField(source='company.company_code')
    company_name = serializers.ReadOnlyField(source='company.companyname')
    user_type = serializers.ReadOnlyField(source='user_type.type_code')
    user_type_name = serializers.ReadOnlyField(source='user_type.type_name')
    class Meta:
        model = UserCompany
        # fields = ['company']
        fields = ('user_company_code','user_code','username','company_code','company_name','user_type','user_type_name')
        read_only_fields = ['user_company_code','company_name','user_type_name','username']


class UserTypeSerializer(BaseSerializer):
    class Meta:
        model = UserType
        fields = ['type_name', 'type_code']



class DestinationSerializer(BaseSerializer):
    # destinationcode = DestinationSerializer(many=False, read_only=True)
    class Meta:
        model = Destination
        # fields = '__all__'
        fields = ['destinationcode','destinationname','statecode']

class PinCodeSerializer(BaseSerializer):
    destinationcode = serializers.ReadOnlyField(source='destinationcode.destinationcode')
    destinationname = serializers.ReadOnlyField(source='destinationcode.destinationname')
    statecode = serializers.ReadOnlyField(source='destinationcode.statecode')
    courier = serializers.ReadOnlyField(source='courier.branchname')
    class Meta:
        model = PinCode
        # fields = '__all__'
        fields = ['pincode','branchcode','oda','topay','courier','pickup','destinationcode','destinationname','statecode','active']
       

class CompanyCourierSerializer(BaseSerializer):
    
    # user_code = serializers.ReadOnlyField(source='user.userid')
    # username = serializers.ReadOnlyField(source='user.username')
    # company_code = serializers.ReadOnlyField(source='company.company_code')
    # company_name = serializers.ReadOnlyField(source='company.companyname')
    # user_type = serializers.ReadOnlyField(source='user_type.type_code')
    # user_type_name = serializers.ReadOnlyField(source='user_type.type_name')
    #  company_courier_mode_code = models.CharField(max_length=50,primary_key=True)
    # userId = models.CharField(max_length=50,null=False,default=None, db_column='userid')
    # company_code = models.ForeignKey(Company,models.DO_NOTHING,null=True,default=None, db_column='company_code')
    # user_type = models.ForeignKey(UserType,models.DO_NOTHING,null=False,default=None, db_column='type_code')
    # shipment_code = models.ForeignKey(ShipmentMode,models.DO_NOTHING,null=False,default=None, db_column='shipment_code')
    

    class Meta:
        model = CompanyCourierMode
        # fields = ('company_courier_mode_code','company_code','user_type','company_name','user_type_name','user_name')
        fields = '__all__'#('userId','company','user_type','shipment_code')
        # read_only_fields = ['user_company_code','company_name','user_type_name','username']

class CourierShipmentModeSerializer(BaseSerializer):
    
    
    class Meta:
        model = CourierShipmentMode
        # fields = ('company_courier_mode_code','company_code','user_type','company_name','user_type_name','user_name')
        fields = '__all__'#('userId','company','user_type','shipment_code')
        # read_only_fields = ['user_company_code','company_name','user_type_name','username']

class CompanySerializer(BaseSerializer):
    company_courier = CompanyCourierSerializer(source='company',many=True,read_only=True)
    # user_type = UserCompanySerializer(many=True,source='company')
    class Meta:
        model = Company
        fields = ['company_code','companyname','company_courier']
        depth = 1

class ClientSerializer(BaseSerializer):
    class Meta:
        model = Client
        fields = ['userid','username','emailid']
        depth = 1

class CourierSerializer(BaseSerializer):
    # courier_shipment = ShipmentModeSerializer(many=True, read_only=True)
    # user_code = serializers.ReadOnlyField(source='companycouriermode__user_type_type_code')
    class Meta:
        model = Courier
        fields = ['branchcode','branchname']
        # fields = ['branchcode','branchname','courier_shipment']
        # read_only_fields = ['courier_code']
        # depth = 1

class ShipmentModeSerializer(BaseSerializer):
    shipment_courier = CourierSerializer(many=True, read_only=True);
    class Meta:
        model = ShipmentMode
        # fields = '__all__'
        fields = ['shipment_mode_code','shipment_mode_name','shipment_courier']
        depth = 1

class ConsigneeSerializer(BaseSerializer):            
    class Meta:
        model = Consignee
        fields = ('conscode','consname','address1','address2','address3','pin','phone','mobile','emailid')
        # extra_kwargs = {'password': {'write_only': True}}
        depth = 1

class UserConsigneeSerializer(BaseSerializer):
    consignee = ConsigneeSerializer(many=False, read_only=True)
    user_code = serializers.ReadOnlyField(source='user.userid')
    username = serializers.ReadOnlyField(source='user.username')
    company_code = serializers.ReadOnlyField(source='company.company_code')
    company_name = serializers.ReadOnlyField(source='company.companyname')
    class Meta:
        model = UserConsignee
        # fields = ('user','company')
        fields = ('user_consignee_code','company_code','user_code','company_name','username','consignee')
        read_only_fields = ['user_consignee_code','company_name','username']
        depth = 1

        
class UserSerializer(BaseSerializer):
    companies = UserCompanySerializer(source='user',many=True, read_only=True)
    class Meta:
        model = User
        fields = ('userid', 'username', 'emailid','password','companies')
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

class AuthSerializer(BaseSerializer):
    user_company = UserCompanySerializer(many=False, read_only=False)
    class Meta:
        model = LocalSession
        fields = ['userid','token','expirey','created','user_company']
        depth = 1

class ChildSerializer(BaseSerializer):
    class Meta:
        model = ChildBooking
        fields = ['subAwbNo','actWG','volWG','dimL','dimH','dimW']
        depth = 1

class BookingSerializer(BaseSerializer):
    courier = CourierSerializer(many=False, read_only=True)
    shipment = ShipmentModeSerializer(many=False, read_only=True)
    consignee = ConsigneeSerializer(many=False, read_only=True)
    client = ClientSerializer(many=False, read_only=True)
    # dim = ChildSerializer(many=True, read_only=True)
    
    class Meta:
        model = BookingWeb
        fields = ('courier','shipment','awbNo','client','companyCode','toFreight','codAmt','insuranceType','EWayNo','invoiceValue'
        ,'invoiceNumber','prodDesc','prodMod','prodIty','prodPiece','prodWeight','user','refid','prodDim','entrydate','consignee','zstatus','dim','shipment_progress')
        depth = 1
        # read_only_fields = ['entrydate']
#  
        # ,'shipment' 'awbType',
        # fields = '__all__'#('userId','company','user_type','shipment_code')
        # read_only_fields = ['user_company_code','company_name','user_type_name','username']



    # {"courier":"DTDC","shipment":"CO","awbNo":"","awbType":"M","client":"RMC_CLNT",
    # "companyCode":"RMC","toFreight":"PREPAID","codAmt":"","insuranceType":"OWNER",
    # "EWayNo":"","invoiceValue":"","invoiceNumber":"","prodDesc":"","prodMod":"SURFACE",
    # "prodIty":"DOX","prodPiece":"2","prodWeight":"","user":"RMC_CLNT",
    # "refid":"","prodDim":"INCH",

    # "consignee":{"conscode":"10001","consname":"COSIGNEE 1", "address1":"ADDRES1", "address2":"ADDRESS2", "address3":"A3", "pin":"110012", "phone":"2300012111", "mobile":"9000000001", "emailid":"MAIL@YAHOO.COM", "state":"null", "save":"true", "oda":"No"},
    # "dim":
    
class AttachmentSerializer(BaseSerializer):
    class Meta:
        model = Attachment
        fields = ['awbno','declarationdata','dfilename','deextn','docketdata','docketfilename','dextn']
