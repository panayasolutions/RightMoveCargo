from rest_framework import serializers

from rightmovecargo.rmcapi.models import Company, Courier, LocalSession, ShipmentMode, User, UserCompany, UserType

class BaseSerializer(serializers.HyperlinkedModelSerializer):
    def test():
        pass

class UserTypeSerializer(BaseSerializer):
    class Meta:
        model = UserType
        fields = ['url', 'user_type_code', 'type_name', 'type_code']
        read_only_fields = ['user_type_code']

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
    user_code = serializers.ReadOnlyField(source='user.user_code')
    user_name = serializers.ReadOnlyField(source='user.username')
    company_code = serializers.ReadOnlyField(source='company.company_code')
    user_type = serializers.ReadOnlyField(source='user_type.user_type_code')
    company_name = serializers.ReadOnlyField(source='company.company_name')
    user_type_name = serializers.ReadOnlyField(source='user_type.user_type_name')
    # winecolor = serializers.CharField(read_only=True, source="branch.company_code"

    class Meta:
        model = UserCompany
        fields = ('user_code','company_code','user_type','company_name','user_type_name','user_name')
        # fields = ('url','user_company_code','branch','user','user_type')
        read_only_fields = ['user_company_code','company_name','user_type_name']
        depth = 1

        
class UserSerializer(BaseSerializer):
    # branchs = UserBranchSerializer(source='user_branch',many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url','username', 'emailid','password' )
        # extra_kwargs = {'password': {'write_only': True}}
        depth = 1

class AuthSerializer(BaseSerializer):
    user_company = UserCompanySerializer(many=False, read_only=True)
    class Meta:
        model = LocalSession
        fields = ['connid','username','token','expirey','created','user_company']
