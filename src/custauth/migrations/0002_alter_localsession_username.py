# Generated by Django 3.2 on 2021-04-27 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localsession',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
