# Generated by Django 5.0.6 on 2024-07-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_user_validation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('client', 'client'), ('owner', 'Owner'), ('admin', 'Admin'), ('super_admin', 'Super Admin')], default='client', max_length=255),
        ),
    ]
