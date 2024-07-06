# Generated by Django 5.0.6 on 2024-07-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_userprofile_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
