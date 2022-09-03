# Generated by Django 3.2.15 on 2022-08-31 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('priority', models.SmallIntegerField()),
                ('status', models.CharField(max_length=255)),
                ('target_delivery_date', models.DateField()),
                ('estimated_delivery_date', models.DateField()),
                ('actual_delivery_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]