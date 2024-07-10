# Generated by Django 5.0.6 on 2024-07-04 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments_and_subscription', '0003_paymentdetails_paypaluserdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfeature',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_features', to='payments_and_subscription.subscription'),
        ),
    ]