# Generated by Django 5.0.6 on 2024-08-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_bookings_booking_timing_bookings_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='booking_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
