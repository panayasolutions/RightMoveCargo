# Generated by Django 2.1.15 on 2021-05-17 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycouriermode',
            name='company_code',
            field=models.ForeignKey(db_column='company_code', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rmcapi.Company'),
        ),
        migrations.AlterField(
            model_name='companycouriermode',
            name='shipment_code',
            field=models.ForeignKey(db_column='shipment_code', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='rmcapi.ShipmentMode'),
        ),
        migrations.AlterField(
            model_name='companycouriermode',
            name='userId',
            field=models.CharField(db_column='userid', default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='companycouriermode',
            name='user_type',
            field=models.ForeignKey(db_column='user_type_code', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='rmcapi.UserType'),
        ),
    ]