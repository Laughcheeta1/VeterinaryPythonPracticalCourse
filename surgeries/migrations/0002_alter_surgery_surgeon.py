# Generated by Django 5.2.3 on 2025-07-02 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgeries', '0001_initial'),
        ('veterinarians', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surgery',
            name='surgeon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veterinarians.veterinarian'),
        ),
    ]
