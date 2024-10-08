# Generated by Django 5.0.6 on 2024-07-24 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_pricegroup'),
        ('services', '0002_company_category'),
        ('userprofile', '0006_userprofile_is_subscribed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='booking_interval_in_minutes',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_company', to='services.company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='designation',
            field=models.CharField(choices=[('employee', 'Employee'), ('consultant', 'Consultant'), ('manager', 'Manager')], default='employee', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_onsite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='online_booking_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='onsite_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='price_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_price_group', to='assets.pricegroup'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='signature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_security_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
