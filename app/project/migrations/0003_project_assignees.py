# Generated by Django 3.2.15 on 2022-09-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_id'),
        ('project', '0002_auto_20220921_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assignees',
            field=models.ManyToManyField(to='employee.Employee'),
        ),
    ]
