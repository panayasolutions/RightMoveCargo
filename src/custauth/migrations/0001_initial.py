# Generated by Django 3.2 on 2021-04-27 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_column='UserId', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=50, unique=True)),
                ('password', models.CharField(db_column='UserPassword', max_length=150)),
                ('usertype', models.CharField(blank=True, db_column='UserType', max_length=10, null=True)),
                ('userrights', models.CharField(blank=True, db_column='UserRights', max_length=10, null=True)),
                ('entrydatetime', models.DateTimeField(blank=True, db_column='EntryDateTime', null=True)),
                ('company', models.CharField(blank=True, db_column='Company', max_length=10, null=True)),
                ('editby', models.CharField(blank=True, db_column='EditBy', max_length=10, null=True)),
                ('editdatetime', models.DateTimeField(blank=True, db_column='EditDateTime', null=True)),
                ('enterby', models.CharField(blank=True, db_column='EnterBy', max_length=10, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', max_length=5, null=True)),
                ('branch', models.CharField(db_column='Branch', max_length=10)),
                ('email', models.EmailField(db_column='EmailID', max_length=255, unique=True)),
                ('resettoken', models.CharField(blank=True, db_column='ResetToken', max_length=255, null=True)),
                ('last_login', models.DateTimeField(db_column='last_login', default=django.utils.timezone.now)),
                ('is_lock', models.BooleanField(db_column='is_lock', default=True)),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default=True)),
                ('is_staff', models.BooleanField(db_column='is_staff', default=True)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'mtUserRevenue',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LocalSession',
            fields=[
                ('connectionid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('authtype', models.CharField(max_length=50, unique=True)),
                ('authtoken', models.CharField(max_length=150)),
                ('authexp', models.DateTimeField(blank=True, null=True)),
                ('authcreated', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'custauth_local_session',
                'managed': True,
            },
        ),
    ]