# Generated by Django 5.0 on 2023-12-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=10)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(default='xyz', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('address', models.CharField(default='xyz', max_length=1000)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('diagnosis', models.CharField(default='fever', max_length=1000)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
