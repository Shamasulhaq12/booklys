# Generated by Django 5.0.6 on 2024-08-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_userprofile_booking_interval_in_minutes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_payment_verified',
            field=models.BooleanField(default=False),
        ),
    ]
