# Generated by Django 5.0 on 2023-12-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_delete_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='time',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
