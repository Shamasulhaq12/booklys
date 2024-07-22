# Generated by Django 5.0.6 on 2024-07-11 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_delete_subcategories'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_category', to='assets.categories'),
        ),
    ]