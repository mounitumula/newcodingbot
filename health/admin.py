from django.contrib import admin

# Register your models here.

from .models import Patient, Employee

admin.register(Patient, Employee)(admin.ModelAdmin)
