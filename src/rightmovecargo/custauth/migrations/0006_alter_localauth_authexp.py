# Generated by Django 3.2 on 2021-04-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custauth', '0005_localauth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localauth',
            name='authexp',
            field=models.DateTimeField(blank=True, db_column='authexp', max_length=10, null=True),
        ),
    ]
