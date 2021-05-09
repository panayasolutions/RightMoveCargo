from custauth.models import User,LocalSession
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
import base64
import binascii
from django.utils import timezone
from rest_framework.response import Response

class Authentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        user = None
        permissions = None
        try:
            authtype,authtoken = authentication.get_authorization_header(request).split();
            
            if not authtype or (authtype.lower() != b'basic' and authtype.lower() != b'bearer'):
                msg = _('Invalid basic header. No credentials provided.')
                raise exceptions.AuthenticationFailed(msg)
            if not authtoken:
                msg = _('Invalid basic header. Credentials string should not contain spaces.')
                raise exceptions.AuthenticationFailed(msg)
            if authtype.lower() == b'basic':
                user,permissions = self.basic_authentication(authtoken,request)
            elif authtype.lower() == b'bearer':
                user,permissions = self.bearer_authentication(authtoken,request)
        except LocalSession.DoesNotExist:
            print('Session not found')
        except (User.DoesNotExist, ValueError) as e:
            print('User not found')
        print(user);
        return (user, permissions)

    def basic_authentication(self,authtoken,request):
        return (None,None);
        # try:
        #     try:
        #         auth_decoded = base64.b64decode(authtoken).decode('utf-8');
        #     except UnicodeDecodeError:
        #         auth_decoded = base64.b64decode(authtoken).decode('latin-1')
        #         auth_parts = auth_decoded.partition(':')
        # except (TypeError, UnicodeDecodeError, binascii.Error):
        #     msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
        #     raise exceptions.AuthenticationFailed(msg) 
        # username, password = auth_parts[0], auth_parts[2];
        # user,permissions = self.authenticate_credentials(username,password,request);

        # try:
        #     # delete all record from LocalSession
        #     authUsers = LocalSession.objects.get(userid=user.id);
        #     authUsers.delete();   
        # except ObjectDoesNotExist:
        #     msg = _('No existing session found.')
        # finally:
        #     localAuth = LocalSession()
        #     localAuth.authtoken =user.username+""+user.id
        #     localAuth.authexp = timezone.now();
        #     localAuth.authcreated = timezone.now();
        #     localAuth.userid = user
        #     localAuth.authtype='Token'
        #     localAuth.save(); 
        #     user.last_login = timezone.now();
        #     user.fail_attempt = 0;
        #     user.save();
        # return (user,user)

    def authenticate_credentials(self, username, password, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        sysuser = User.objects.get(username=username);
        if sysuser is None:
            raise exceptions.AuthenticationFailed(_('User not exists, Please signoff first.'))
        if not sysuser.is_active:
            raise exceptions.AuthenticationFailed(_('User is not verfied.'))
        if sysuser.is_lock:
            raise exceptions.AuthenticationFailed(_('User is locked,please check with admin'))

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }
        user = authenticate(request=request, **credentials);
        if user is None:
            sysuser.fail_attempt = sysuser.fail_attempt+1;
            sysuser.last_login = timezone.now();
            if sysuser.fail_attempt >4:
                sysuser.is_lock = True;
            sysuser.save();
            raise exceptions.AuthenticationFailed(_('Invalid credentials.'))
        return (user, None)


    def bearer_authentication(self,authtoken,request):
        localses = LocalSession.objects.get(token=authtoken.decode('utf-8'))
        sysuser = localses.userid
        if sysuser is None:
            raise exceptions.AuthenticationFailed(_('User not exists, Please signoff first.'))
        if not sysuser.is_active:
            raise exceptions.AuthenticationFailed(_('User is not verfied.'))
        if sysuser.is_lock:
            raise exceptions.AuthenticationFailed(_('User is locked,please check with admin'))
        return (sysuser,None)

    def session_authentication(self,authtoken,request):
        localses = LocalSession.objects.get(authtoken=authtoken.decode('utf-8'),authtype='SESSION');
        sysuser = localses.userid;
        if sysuser is None:
            raise exceptions.AuthenticationFailed(_('User not exists, Please signoff first.'))
        if not sysuser.is_active:
            raise exceptions.AuthenticationFailed(_('User is not verfied.'))
        if sysuser.is_lock:
            raise exceptions.AuthenticationFailed(_('User is locked,please check with admin'))
        return (sysuser,None)