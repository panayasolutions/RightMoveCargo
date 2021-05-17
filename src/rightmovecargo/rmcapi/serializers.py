from rest_framework import serializers

from rightmovecargo.rmcapi.models import LocalSession, User

class BaseSerializer(serializers.HyperlinkedModelSerializer):
    def test():
        pass

class AuthSerializer(BaseSerializer):
    class Meta:
        model = LocalSession
        fields = ['user_code','token','expirey','created','user_branch']
