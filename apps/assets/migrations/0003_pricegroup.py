# Generated by Django 5.0.6 on 2024-07-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_delete_subcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Price Group',
                'verbose_name_plural': 'Price Groups',
                'db_table': 'price_group',
            },
        ),
    ]