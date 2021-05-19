# Generated by Django 2.1.15 on 2021-05-19 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmcapi', '0006_auto_20210519_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercompany',
            old_name='userId',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='localsession',
            name='user_compnay',
        ),
        migrations.AddField(
            model_name='localsession',
            name='user_company',
            field=models.ForeignKey(db_column='company', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rmcapi.UserCompany'),
        ),
        migrations.AlterUniqueTogether(
            name='usercompany',
            unique_together={('user', 'user_type', 'company')},
        ),
    ]
