# Generated by Django 4.2.9 on 2024-04-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0028_alter_fine_list_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
