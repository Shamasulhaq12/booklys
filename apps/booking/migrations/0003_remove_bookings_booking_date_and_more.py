# Generated by Django 5.0.6 on 2024-08-22 13:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_bookings_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='bookings',
            name='booking_timing',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
