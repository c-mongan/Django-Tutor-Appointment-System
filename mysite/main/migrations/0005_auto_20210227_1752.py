# Generated by Django 3.1.5 on 2021-02-27 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210227_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date & Time'),
        ),
    ]