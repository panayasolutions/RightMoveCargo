"""rightmovecargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from rest_framework import routers
from rightmovecargo.rmcapi.serializers import UserConsigneeSerializer

from rightmovecargo.rmcapi.viewsets.authviewset import AuthViewSet
from rightmovecargo.rmcapi.viewsets.bookingviewset import BookingViewSet
from rightmovecargo.rmcapi.viewsets.clientsviewset import ClientViewSet
from rightmovecargo.rmcapi.viewsets.companycourierviewset import CompanyCourierViewSet
from rightmovecargo.rmcapi.viewsets.companyviewset import CompanyViewSet
from rightmovecargo.rmcapi.viewsets.consigneeviewset import ConsigneeViewSet
from rightmovecargo.rmcapi.viewsets.couriershipmentmodeviewset import CourierShipmentModeViewSet
from rightmovecargo.rmcapi.viewsets.courierviewset import CourierViewSet
from rightmovecargo.rmcapi.viewsets.shipmentmodeviewset import ShipmentModeViewSet
from rightmovecargo.rmcapi.viewsets.usercompanyviewset import UserCompanyViewSet
from rightmovecargo.rmcapi.viewsets.userconsigneeviewset import UserConsigneeViewSet
from rightmovecargo.rmcapi.viewsets.usertypeviewset import UserTypeViewSet
from rightmovecargo.rmcapi.viewsets.userviewset import UserViewSet

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet)
router.register(r'user', UserViewSet)
router.register(r'consignee', ConsigneeViewSet)
router.register(r'client', ClientViewSet)
# router.register(r'usercompany', UserCompanyViewSet)
# router.register(r'userconsignee', UserConsigneeViewSet)
# router.register(r'companycourier', CompanyCourierViewSet)
# router.register(r'couriershipment', CourierShipmentModeViewSet)

router.register(r'usertype', UserTypeViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'courier', CourierViewSet)
router.register(r'shipment', ShipmentModeViewSet)
router.register(r'booking', BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('custauth.urls')),
]


# import secrets
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# import os
# from base64 import b64decode, b64encode


# def updatepwd(pwd, tokenstr):

#     print(tokenstr)
#     keyval = constants.KEYVAL
#     iv = os.urandom(constants.BLOCKSIZE)
#     print(iv)
#     aes = AES.new(keyval,AES.MODE_CBC, iv)
#     enpwd = aes.encrypt(pad(str(pwd).encode(), constants.BLOCKSIZE))
#     print(enpwd)
