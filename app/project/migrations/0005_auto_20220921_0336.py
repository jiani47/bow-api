# Generated by Django 3.2.15 on 2022-09-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_project_assignees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='actual_delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='target_delivery_date',
            field=models.DateField(null=True),
        ),
    ]
