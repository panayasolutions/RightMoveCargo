from django.db import models;
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
    Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    class Meta:
        managed = True
        db_table = 'mtUserRevenue'
    id = models.CharField(primary_key=True,db_column='UserId',max_length=50,default=uuid.uuid4)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50,unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='UserPassword', max_length=150)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    userrights = models.CharField(db_column='UserRights', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime',default=timezone.now, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10, blank=True, null=True)  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime',default=timezone.now, blank=True, null=True)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=5, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10)  # Field name made lowercase.
    email = models.EmailField(db_column='EmailID', max_length=255,unique=True)  # Field name made lowercase.
    resettoken = models.CharField(db_column='ResetToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
        
    #Custom Field required
    fail_attempt = models.IntegerField(db_column='fail_attempt',default=0)
    last_login = models.DateTimeField(db_column='last_login',default=timezone.now)  # Field name made lowercase.
    is_lock = models.BooleanField(db_column='is_lock',default=True) # Field name made lowercase. This field type is a guess.
    is_superuser = models.BooleanField(db_column='is_superuser',default=False) # Field name made lowercase. This field type is a guess.
    is_staff = models.BooleanField(db_column='is_staff',default=False)  # Field name made lowercase. This field type is a guess.
    is_active = models.BooleanField(db_column='is_active',default=False)  # Field name made lowercase. This field type is a guess.

    objects = UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','password']
    def get_full_name(self):
        return self.username+""+self.email

    def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))
    # /*def __str__(self):
    #     return self.username+"("+self.email+")"
    # */



class LocalSession(models.Model):
    connid = models.CharField(primary_key=True, max_length=50,default=uuid.uuid4,db_column='connectionid')
    authtype = models.CharField(max_length=50,db_column='authtype')
    token = models.CharField(max_length=150,db_column='authtoken')
    expirey = models.DateTimeField(blank=True, null=True,db_column='authexp')
    created = models.DateTimeField(blank=True, null=True,db_column='authcreated')
    userid = models.ForeignKey(User, models.DO_NOTHING,db_column='userid')
    username = ''

    class Meta:
        managed = True
        db_table = 'custauth_local_session'