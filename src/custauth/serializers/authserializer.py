from custauth.models import LocalSession
from custauth.serializers.baseserializer import BaseSerializer
class AuthSerializer(BaseSerializer):
    class Meta:
        model = LocalSession
        fields = ['username','token','expirey','created']
