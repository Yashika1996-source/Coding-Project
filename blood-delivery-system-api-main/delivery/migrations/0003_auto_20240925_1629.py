# Generated by Django 3.2.10 on 2024-09-25 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20240925_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverystaff',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='deliverystaff',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=10),
        ),
        migrations.AddField(
            model_name='deliverystaff',
            name='license_number',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='deliverystaff',
            name='vehicle_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='deliverystaff',
            name='vehicle_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='deliverystaff',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='deliverystaff',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]