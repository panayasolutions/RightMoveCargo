from custauth.models import User
from custauth.serializers.baseserializer import BaseSerializer
class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','password','usertype','userrights','company','branch', 'groups']
        extra_kwargs = {'password': {'write_only': True}}