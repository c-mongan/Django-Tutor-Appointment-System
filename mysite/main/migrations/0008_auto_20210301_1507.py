# Generated by Django 3.1.5 on 2021-03-01 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210301_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='author',
            new_name='student',
        ),
    ]