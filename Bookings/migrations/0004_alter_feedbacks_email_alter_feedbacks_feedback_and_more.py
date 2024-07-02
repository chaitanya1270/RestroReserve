# Generated by Django 5.0.6 on 2024-07-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
