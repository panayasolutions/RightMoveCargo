from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from rightmovecargo.custauth.models import User
from custauth.serializers.userserializer import UserSerializer
from custauth.serializers.groupserializer import GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    