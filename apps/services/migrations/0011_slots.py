# Generated by Django 5.0.6 on 2024-09-15 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_remove_companystaff_staff_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('work_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_slots', to='services.workschedule')),
            ],
            options={
                'verbose_name': 'Slot',
                'verbose_name_plural': 'Slots',
            },
        ),
    ]
