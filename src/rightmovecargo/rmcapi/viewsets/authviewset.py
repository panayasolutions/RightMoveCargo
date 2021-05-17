from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
import base64
import binascii
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rightmovecargo.rmcapi.models import LocalSession, User
from rightmovecargo.rmcapi.serializers import AuthSerializer
from rightmovecargo.rmcapi.viewsets.baseviewset import BaseViewSet
# from django.contrib.auth.tokens import default_token_generator   

class AuthViewSet(BaseViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalSession.objects.all()
    serializer_class = AuthSerializer
    permission_classes = []
    def create(self, request):
        try:
            user=None;
            localAuth=None
            authtype,authtoken = authentication.get_authorization_header(request).split();
            if not authtype or (authtype.lower() != b'basic' and authtype.lower() != b'bearer'):
                msg = _('Invalid basic header. No credentials provided.')
            elif not authtoken:
                msg = _('Invalid basic header. Credentials string should not contain spaces.')
            elif authtype.lower() == b'basic':
                user,localAuth,msg = self.basic_authentication(authtoken,request)
            elif authtype.lower() == b'bearer':
                user,localAuth,msg = self.bearer_authentication(authtoken,request)
        except LocalSession.DoesNotExist:
            msg = _('Session not found')
        except (User.DoesNotExist ,ValueError) as e:
            msg = _('User not found')
        if msg != None:
           return self.onError("",msg,status.HTTP_403_FORBIDDEN) 
        serializer = self.get_serializer(localAuth)
        # serializer.is_valid(localAuth);
        return  self.onSuccess([serializer.data],user.username+" authenticate successfully",status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            msg = None;
            user=None;
            localAuth=None
            authtype,authtoken = authentication.get_authorization_header(request).split();
            if not authtype or (authtype.lower() != b'basic' and authtype.lower() != b'bearer'):
                msg = _('Invalid basic header. No credentials provided.')
            if not authtoken:
                msg = _('Invalid basic header. Credentials string should not contain spaces.')
            elif authtype.lower() == b'bearer':
                user,localAuth,msg = self.logout(authtoken,request)
            else:
                msg = _('No session found')
        except LocalSession.DoesNotExist:
            msg = _('Session not found')
        except (User.DoesNotExist ,ValueError) as e:
            msg = _('User not found')
        if msg != None:
           return self.onError("",msg,status.HTTP_403_FORBIDDEN) 
        return  self.onSuccess('',msg,status.HTTP_200_OK)
        
    def list(self, request, *args, **kwargs):
        try:
            msg = None;
            user= None;
            localAuth=None
            authtype,authtoken = authentication.get_authorization_header(request).split();
            if not authtype or (authtype.lower() != b'bearer'):
                msg = _('Invalid basic header. No credentials provided.')
            if not authtoken:
                msg = _('Invalid basic header. Credentials string should not contain spaces.')
            elif authtype.lower() == b'bearer':
                localAuth = LocalSession.objects.get(token=authtoken.decode('utf-8'),authtype='TOKEN');
                localAuth.username=localAuth.userid.get_username();
                localAuth.token = "Bearer "+localAuth.token;
            else:
                msg = _('No session found')
        except LocalSession.DoesNotExist:
            msg = _('Session not found')
        except (User.DoesNotExist ,ValueError) as e:
            msg = _('Aunthorized request')
        if msg != None:
            return self.onError("",msg,status.HTTP_403_FORBIDDEN) 
        serializer = self.get_serializer(localAuth)
        return self.onSuccess(serializer.data,msg,status.HTTP_200_OK)

    def authenticate_credentials(self, username, password, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        msg = None
        sysuser = User.objects.get(userid=username);
        if sysuser is None:
            return (None,None,'User not exists, Please signoff first.')
        if not sysuser.is_active:
            return (None,None,'User is not verfied.')
        # if sysuser.is_lock:
        #     return (None,None,'User is locked,please check with admin')

        
        user = self.user_credentials_validation(username=username,password=password);
        if user is None:
            # sysuser.fail_attempt = sysuser.fail_attempt+1;
            # sysuser.last_login = timezone.now();
            # if sysuser.fail_attempt >4:
            #     sysuser.is_lock = True;
            # sysuser.save();
            return (None,None,'Invalid credentials.')
        return (user, None,msg)

    def basic_authentication(self,authtoken,request):
        try:
            try:
                auth_decoded = base64.b64decode(authtoken).decode('utf-8');
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(authtoken).decode('latin-1')
            auth_parts = auth_decoded.partition(':')
        except (TypeError, UnicodeDecodeError, binascii.Error):
            return (None,None,'Invalid basic header. Credentials not correctly base64 encoded.')
        username, password = auth_parts[0], auth_parts[2];
        
        user,permissions,msg = self.authenticate_credentials(username,password,request);
        if user is None:
            return (None,None,msg)
        try:
            # delete all record from LocalSession
            authUsers = LocalSession.objects.get(username=user.username);
            authUsers.delete();   
        except ObjectDoesNotExist:
            #return (None,None,'No existing session found.')
            print('sdf');
        finally:
            print(user.username+""+user.password)
            localAuth = LocalSession()
            localAuth.token = user.username+""+user.password #default_token_generator.make_token(user);
            localAuth.username = user.username
            localAuth.connid = self.create_id('CONN')
            localAuth.created = timezone.now();
            localAuth.expirey = timezone.now();
            localAuth.save()
            user.editdatetime = timezone.now();
            user.editby = '';
            user.save();
            localAuth.token = "Bearer "+localAuth.token;
        return (user,localAuth,msg)

    def bearer_authentication(self,authtoken,request):
        localses = LocalSession.objects.get(token=authtoken.decode('utf-8'),authtype='TOKEN');
        sysuser = localses.username;
        localses.username=sysuser.get_username();
        localses.token = "Bearer "+localses.token;
        print(request.data);
        if request.data != {}:
            try:
                branch = Branch.objects.get(branch_code = request.data['branch_code']);
                user_type = UserType.objects.get(user_type_code = request.data['user_type']);
                userBranch = UserBranch.objects.get(user=sysuser,branch=branch,user_type=user_type);
                sysuser.modified_by = sysuser
                localses.user_branch = userBranch;
                # localses.update()
                LocalSession.objects.filter(connid = localses.connid).update(user_branch = userBranch)
                # LocalSession.objects.update()
                # serializer = self.get_serializer(localses);
            except (User.DoesNotExist,Branch.DoesNotExist,UserBranch.DoesNotExist,KeyError) as e:
                return (sysuser,localses,'Branch does not exist')
        msg = None;
        if sysuser is None:
            return (None,None,'User not exists, Please signoff first.')
        if not sysuser.is_active:
            return (None,None,'User is not verfied.')
        if sysuser.is_lock:
            return (None,None,'User is locked,please check with admin')
        return (sysuser,localses,msg)

    def session_authentication(self,authtoken,request):
        localses = LocalSession.objects.get(token=authtoken.decode('utf-8'),authtype='SESSION');
        sysuser = localses.userid;
        if sysuser is None:
            return (None,None,'User not exists, Please signoff first.')
        if not sysuser.is_active:
            return (None,None,'User is not verfied.')
        if sysuser.is_lock:
            return (None,None,'User is locked,please check with admin')
        return (sysuser,localses,msg)

    def logout(self,authtoken,request):
        localses = LocalSession.objects.get(token=authtoken.decode('utf-8'));
        sysuser = localses.userid;
        if sysuser is None:
            return (None,None,'User not exists, Please signoff first.')
        if not sysuser.is_active:
            return (None,None,'User is not verfied.')
        if sysuser.is_lock:
            return (None,None,'User is locked,please check with admin')
        localses.delete()
        return (sysuser,localses,sysuser.username+' logout successfully')