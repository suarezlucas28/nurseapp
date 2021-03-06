# Generated by Django 3.0 on 2020-05-19 15:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VitalSigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('minValue', models.IntegerField()),
                ('maxValue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SignsRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2020, 5, 19, 15, 16, 4, 246954, tzinfo=utc))),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentValue', models.IntegerField()),
                ('signRegistration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SignsRegistration')),
                ('vitalSigns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VitalSigns')),
            ],
        ),
    ]
