# Generated by Django 2.1.7 on 2019-11-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_employee_reporting_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
    ]
