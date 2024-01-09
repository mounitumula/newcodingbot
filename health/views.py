from django.shortcuts import render, redirect
from datetime import date, datetime
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from . import models
import re


# Create your views here.
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    x = re.match(pattern, email)
    if x:
        return True
    else:
        return False


def validate_phone_number(phone_number):
    pattern = r'^(?:\+91|0)?(?:\d{10}|0\d{10}|0\d{2}-\d{8})$'
    x = re.match(pattern, phone_number)
    if x:
        return True
    else:
        return False


def home(request):
    return render(request, "index.html")


def register(request):
    # messages.success(request, "Welcome to Registration Form. Please enter your Details")
    if request.method == "POST":
        # emp_id = request.POST.get("employee_id")
        name = request.POST.get('employee_name')
        age = request.POST.get("age")
        city = request.POST.get("city")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_email_valid = validate_email(email)
        if not is_email_valid:
            return HttpResponse("<h1> Invalid Email Address, please Enter Valid email<h1>")
        is_phone_number_valid = validate_phone_number(phone_number)
        if not is_phone_number_valid:
            return HttpResponse("<h1> not a valid phone number, please enter valid phone number<h1>")
        # create a user object
        employee = models.Employee(employee_name=name, age=age, city=city,
                                   phone_number=phone_number, email=email, password=password)
        employee.save()
        messages.success(request, "User Added Successfully")
        return render(request, "patient.html")
    else:
        return render(request, "register.html")


def login(request):
    # messages.success(request, "Welcome to Registration Form. Please enter your Details")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # get user object
        employee = models.Employee.objects.filter(email=email)
        if employee:
            for data in employee:
                db_password = data.password
                if password == db_password:
                    messages.success(request, "User Login is Successful")
                    return render(request, "patient.html")
            messages.error(request, "Incorrect username and password, please try again")
            return render(request, "login.html")
        else:
            return HttpResponse("<h2> login unsuccessful</h2>")
    else:
        return render(request, "login.html")


def patient(request):
    # messages.success(request, "Welcome to Registration Form. Please enter your Details")
    if request.method == "POST":
        name = request.POST.get('patient_name')
        age = request.POST.get("age")
        address = request.POST.get("äddress")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        diagnosis = request.POST.get("diagnosis")
        date = request.POST.get("data")
        time = request.POST.get("time")
        # create a user object
        patient = models.Patient(patient_name=name, age=age, address=address,
                                 phone_number=phone_number, email=email, diagnosis=diagnosis, date=date, time=time)
        patient.save()
        messages.success(request, "Patient Added Successfully")
        return render(request, "patient.html")
    else:
        return redirect("/")


def display(request):
    if request.method == "GET":
        patients_data = models.Patient.objects.all()
        context = {"data": patients_data}
        return render(request, "display.html", context)


def book(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        patients_data = models.Patient.objects.all()
        present = False
        if patients_data:
            for data in patients_data:
                if email == data.email:
                    present = True
                    print("patient info already exits in db")
                    data.date = date
                    data.time = time
                    data.appointment_status = "Booked"
                    data.save()
                    messages.success(request, "Appointment Updated Successfully")
                    return render(request, "messages.html")
            if not present:
                name = request.POST.get('name')
                phone_number = request.POST.get("phone")
                age = request.POST.get("age")
                email = request.POST.get("email")
                address = request.POST.get("address")
                diagnosis = request.POST.get("diagnosis")
                appointment_status = "Booked"
                patient_d = models.Patient(patient_name=name, age=age, address=address,
                                           phone_number=phone_number, email=email, diagnosis=diagnosis, date=date,
                                           time=time, appointment_status=appointment_status)
                patient_d.save()
                messages.success(request, "Patient Added Successfully")
                return render(request, "messages.html")
    elif request.method == 'GET':
        return render(request, "book.html")
    else:
        HttpResponseBadRequest('You can not do that')


def cancel_appointment(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        patients_data = models.Patient.objects.all()
        present = False
        if patients_data:
            for data in patients_data:
                if email == data.email:
                    present = True
                    print("cancel appointment if count is less than 2")
                    no_of_cancellation = data.no_of_cancellation
                    booking_date = data.date
                    if booking_date:
                        booking_date = datetime.strptime(booking_date, '%Y-%m-%d')
                        current_date = datetime.today()
                        delta = current_date - booking_date
                        if delta.days <= 30:
                            if no_of_cancellation >= 2:
                                messages.warning(request, "More than two cancellations are not allowed in a month")
                            else:
                                data.no_of_cancellation = no_of_cancellation + 1
                                data.appointment_status = "cancelled"
                                data.cancellation_date = current_date
                                data.date = ''
                                data.time = ''
                                data.save()
                                messages.success(request, "Appointment cancelled successfully")
                        else:
                            data.no_of_cancellation = 1
                            data.appointment_status = "cancelled"
                            data.cancellation_date = current_date
                            data.date = ''
                            data.time = ''
                            data.save()
                            messages.success(request, "Appointment cancelled successfully")
                    else:
                        messages.warning(request, "No Bookings for below id")
                    return render(request, "messages.html")

            if not present:
                messages.error(request, "Patient Not present")
                return render(request, "messages.html")
    elif request.method == 'GET':
        return render(request, "cancel.html")
    else:
        HttpResponseBadRequest('You can not do that')
