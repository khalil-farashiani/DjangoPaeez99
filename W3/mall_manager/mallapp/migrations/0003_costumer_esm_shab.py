# Generated by Django 3.1.2 on 2020-11-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallapp', '0002_auto_20201105_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='esm_shab',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
