# Generated by Django 2.1.15 on 2021-05-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0004_auto_20210530_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbbookingchild',
            name='masterawbno',
            field=models.CharField(db_column='masterawbno', max_length=50),
        ),
    ]