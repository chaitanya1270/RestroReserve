# Generated by Django 5.0.6 on 2024-06-28 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0003_tablestatus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableStatus',
            new_name='Table_Status',
        ),
    ]