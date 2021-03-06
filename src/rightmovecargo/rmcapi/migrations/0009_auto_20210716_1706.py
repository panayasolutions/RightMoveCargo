# Generated by Django 2.1.15 on 2021-07-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0008_auto_20210716_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('destinationcode', models.CharField(db_column='DestinationCode', max_length=10, primary_key=True, serialize=False)),
                ('destinationname', models.CharField(db_column='DestinationName', max_length=50)),
                ('statecode', models.CharField(db_column='StateCode', max_length=5)),
                ('enterby', models.CharField(db_column='EnterBy', max_length=10)),
                ('entrydatetime', models.DateTimeField(db_column='EntryDatetime')),
                ('oda', models.CharField(db_column='ODA', max_length=5)),
            ],
            options={
                'db_table': 'mtDestination',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PinCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(db_column='PinCode', max_length=6, null=True)),
                ('courier', models.CharField(db_column='CourierCode', max_length=10, null=True)),
                ('branchcode', models.CharField(db_column='BranchCode', max_length=10, null=True)),
                ('oda', models.CharField(db_column='ODA', max_length=10, null=True)),
                ('topay', models.CharField(db_column='ToPayorCod', max_length=10, null=True)),
                ('compnay', models.CharField(db_column='CompanyCode', max_length=10, null=True)),
                ('pickup', models.CharField(db_column='PickUp', max_length=10, null=True)),
                ('enterby', models.CharField(db_column='EnterBy', max_length=10)),
                ('entrydatetime', models.DateTimeField(db_column='EntryDatetime', default=None)),
                ('active', models.CharField(db_column='Active', max_length=5, null=True)),
                ('destinationcode', models.CharField(db_column='DestinationCode', max_length=10, null=True)),
            ],
            options={
                'db_table': 'mtPin',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='pincode',
            unique_together={('pincode', 'courier')},
        ),
    ]
