from django.shortcuts import render, redirect
from .models import RegisterStudent
# Create your views here.


def registerStudent(request):
    templates = 'register.html'
    context = {
        'error': 'all fields are required'
    }

    if request.method == 'POST':
        if request.POST['firstName'] and request.POST['lastName']  and request.POST['grade']  and request.POST['phoneNumber'] and request.POST['fatherName'] and request.POST['studentId'] :
            register = RegisterStudent()
            register.phoneNumber = request.POST['phoneNumber']
            register.firstName = request.POST['firstName']
            register.lastName = request.POST['lastName']
            register.fathersName = request.POST['fatherName']
            register.grade = request.POST['grade']
            register.studentId = request.POST['studentId']
            register.save()
            return redirect('home')

        else:
            return render(request, templates , context) 

    else:
        return render(request, templates , context)