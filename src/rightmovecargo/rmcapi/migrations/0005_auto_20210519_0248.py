# Generated by Django 2.1.15 on 2021-05-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0004_auto_20210519_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='user_type_code',
        ),
        migrations.AlterField(
            model_name='usertype',
            name='type_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
