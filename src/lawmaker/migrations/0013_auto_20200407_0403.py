# Generated by Django 2.2.10 on 2020-04-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawmaker', '0012_auto_20200407_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidacy',
            name='military_info',
            field=models.CharField(blank=True, max_length=30, verbose_name='병역'),
        ),
    ]