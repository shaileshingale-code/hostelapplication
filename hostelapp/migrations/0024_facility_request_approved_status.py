# Generated by Django 4.2.9 on 2024-02-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0023_facility_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_request',
            name='approved_status',
            field=models.IntegerField(default=0),
        ),
    ]
