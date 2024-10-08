# Generated by Django 5.0.6 on 2024-08-26 20:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_servicefeedback_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='booking_timing',
        ),
        migrations.AddField(
            model_name='bookings',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='end_booking_slot',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='start_booking_slot',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
