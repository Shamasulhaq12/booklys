# Generated by Django 4.2.15 on 2024-09-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_journals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='end_booking_slot',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='start_booking_slot',
            field=models.TimeField(blank=True, null=True),
        ),
    ]