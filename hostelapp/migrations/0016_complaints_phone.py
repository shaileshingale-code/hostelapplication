# Generated by Django 4.2.9 on 2024-02-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0015_complaints'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
