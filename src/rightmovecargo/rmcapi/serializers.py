from rest_framework import serializers

from rightmovecargo.rmcapi.models import Company, Consignee, Courier, LocalSession, ShipmentMode, User, UserCompany, UserConsignee, UserType

class BaseSerializer(serializers.HyperlinkedModelSerializer):
    def test():
        pass

class UserTypeSerializer(BaseSerializer):
    class Meta:
        model = UserType
        fields = ['url', 'type_name', 'type_code']
        read_only_fields = ['type_code']

class CompanySerializer(BaseSerializer):
    class Meta:
        model = Company
        fields = ['company_code','companyname']
        read_only_fields = ['company_code']

class CourierSerializer(BaseSerializer):
    class Meta:
        model = Courier
        fields = ['url','courier_code','courier_name']
        read_only_fields = ['courier_code']

class ShipmentModeSerializer(BaseSerializer):
    class Meta:
        model = ShipmentMode
        fields = ['url','shipment_mode_code','shipment_mode_name']
        read_only_fields = ['shipment_mode_code']

class UserCompanySerializer(BaseSerializer):
    # user_type = UserTypeSerializer(many=False, read_only=True)
    user_code = serializers.ReadOnlyField(source='user.userid')
    username = serializers.ReadOnlyField(source='user.username')
    company_code = serializers.ReadOnlyField(source='company.company_code')
    company_name = serializers.ReadOnlyField(source='company.companyname')
    user_type = serializers.ReadOnlyField(source='user_type.type_code')
    user_type_name = serializers.ReadOnlyField(source='user_type.type_name')
    # user_type = serializers.CharField(read_only=True, source="type_name")
    # user_company_code = models.CharField(max_length=50,primary_key=True)
    # userId = models.ForeignKey(User,models.DO_NOTHING,null=False,default=None, db_column='userid')
    # user_type = models.ForeignKey(UserType,models.DO_NOTHING,null=False,default=None,db_column='type_code')
    # company = models.ForeignKey(Company,models.DO_NOTHING,null=True,default=None,db_column='company_code')


    class Meta:
        model = UserCompany
        # fields = ('company_courier_mode_code','company_code','user_type','company_name','user_type_name','user_name')
        fields = ('company_code','user_code','user_type','company_name','username','user_type_name')
        read_only_fields = ['user_company_code','company_name','user_type_name','username']
        depth = 1

class ConsigneeSerializer(BaseSerializer):            
    class Meta:
        model = Consignee
        fields = ('consname','address1','address2','address3','pin','phone','mobile','emailid')
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
    # company = UserCompanySerializer(source='user_branch',many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url','userid', 'username', 'emailid','password')
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

class AuthSerializer(BaseSerializer):
    user_company = UserCompanySerializer(many=True, read_only=True)
    class Meta:
        model = LocalSession
        fields = ['userid','token','expirey','created','user_company']
