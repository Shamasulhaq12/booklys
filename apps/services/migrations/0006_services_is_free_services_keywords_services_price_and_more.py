# Generated by Django 5.0.6 on 2024-08-22 11:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_rename_t_services_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        # migrations.AddField(
        #     model_name='services',
        #     name='keywords',
        #     field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None),
        # ),
        migrations.AddField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='services',
            name='price_type',
            field=models.CharField(choices=[('fixed', 'Fixed'), ('variable', 'Variable')], default='fixed', max_length=255),
        ),
        migrations.DeleteModel(
            name='ServicePrice',
        ),
    ]
