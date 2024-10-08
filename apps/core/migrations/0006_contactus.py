# Generated by Django 5.0.6 on 2024-09-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
                'db_table': 'contact_us',
                'ordering': ['-id'],
                'indexes': [models.Index(fields=['-id'], name='contact_us_id_afc968_idx'), models.Index(fields=['-created_at'], name='contact_us_created_87baa7_idx')],
            },
        ),
    ]
