from django.db import models


# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=1000, default="xyz")
    phone_number = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    diagnosis = models.CharField(max_length=1000, default="fever")
    date = models.CharField(max_length=1000, null=True, blank=True)
    time = models.CharField(max_length=1000, null=True, blank=True)
    no_of_cancellation = models.IntegerField(default=0)
    appointment_status = models.CharField(max_length=1000, null=True, blank=True)
    cancellation_date = models.CharField(max_length=1000, null=True, blank=True)


class Employee(models.Model):
    employee_name = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=6, default="xyz")

