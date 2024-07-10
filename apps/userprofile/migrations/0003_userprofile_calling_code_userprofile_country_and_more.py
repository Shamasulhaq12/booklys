# Generated by Django 5.0.6 on 2024-07-04 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('userprofile', '0002_userprofile_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='calling_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_country_codes', to='assets.callingcodewithname'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_countries', to='assets.countries'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscription_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscription_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]