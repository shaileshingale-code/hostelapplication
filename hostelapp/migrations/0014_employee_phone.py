# Generated by Django 4.2.9 on 2024-02-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0013_remove_employee_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
