# Generated by Django 2.2.10 on 2020-04-05 17:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawmaker', '0007_auto_20200405_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='activelawmaker',
            name='representative_bill',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=[], max_length=20), default=[], size=None),
            preserve_default=False,
        ),
    ]
