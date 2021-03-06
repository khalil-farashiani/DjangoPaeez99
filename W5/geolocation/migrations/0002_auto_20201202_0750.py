# Generated by Django 3.1.2 on 2020-12-02 07:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='alley',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='کوچه'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='address',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='موقعیت جغرافیایی'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='پلاک'),
        ),
        migrations.AlterField(
            model_name='address',
            name='poste_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='کدپستی'),
        ),
        migrations.AlterField(
            model_name='address',
            name='priority_address',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, choices=[('tehran', 'تهران'), ('alborz', 'البرز'), ('markazi', 'مرکزی')], max_length=20, null=True, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='خیابان'),
        ),
    ]
