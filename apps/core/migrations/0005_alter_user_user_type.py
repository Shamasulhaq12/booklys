# Generated by Django 5.0.6 on 2024-07-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('client', 'client'), ('owner', 'Owner'), ('staff', 'Staff'), ('admin', 'Admin'), ('super_admin', 'Super Admin')], default='client', max_length=255),
        ),
    ]
