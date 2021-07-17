# Generated by Django 2.1.15 on 2021-05-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0002_auto_20210523_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingweb',
            old_name='ewaybillno',
            new_name='EWayNo',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='awbno',
            new_name='awbNo',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='clientcode',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='cod',
            new_name='codAmt',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='companycode',
            new_name='companyCode',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='couriercode',
            new_name='courier',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='riskcoveredby',
            new_name='insuranceType',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='invoicenumber',
            new_name='invoiceNumber',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='invoicevalue',
            new_name='invoiceValue',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='productdesc',
            new_name='prodDesc',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='dimensions',
            new_name='prodDim',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='doctype',
            new_name='prodIty',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='mode',
            new_name='prodMod',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='pcs',
            new_name='prodPiece',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='actweight',
            new_name='prodWeight',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='referenceid',
            new_name='refid',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='topay',
            new_name='toFreight',
        ),
        migrations.RenameField(
            model_name='bookingweb',
            old_name='submitteduser',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='branchcode',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='branchname',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='height',
            new_name='dimH',
        ),
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='length',
            new_name='dimL',
        ),
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='width',
            new_name='dimW',
        ),
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='actweight',
            new_name='actWG',
        ),
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='volweight',
            new_name='volWG',
        ),
        
        migrations.RenameField(
            model_name='ChildBooking',
            old_name='childawb',
            new_name='subAwbNo',
        ),
        migrations.AddField(
            model_name='consignee',
            name='clients',
            field=models.ManyToManyField(related_name='clients', through='rmcapi.UserConsignee', to='rmcapi.User'),
        ),
        migrations.AlterUniqueTogether(
            name='ChildBooking',
            unique_together={('masterawbno', 'subAwbNo')},
        ),
    ]
