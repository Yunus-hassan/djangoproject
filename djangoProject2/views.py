from django.shortcuts import render, redirect
from .models import Student
from.models import Teacher

def aboutpage(request):
    return render(request, "about.html")


def servicespage(request):
    return render(request, "services.html")


def projectspage(request):
    return render(request, "projects.html")


def blogpage(request):
    return render(request, "blog.html")

def insertdata(request):
    if request.method == "POST":
        fullname = request.POST.get('fullnames')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        classcode = request.POST.get('classcode')

        query = Student(fullname = fullname, age= age, email=email, phone=phone, classcode=classcode)
        query.save()
        return redirect("/")
