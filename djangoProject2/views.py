from django.shortcuts import render, redirect
from .models import People


def servicespage(request):
    return render(request, "services.html")


def projectspage(request):
    return render(request, "projects.html")


# function to delete data
def deletedata(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "about.html")


# function to update our record
def updatedata(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = People.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.age = age
        edit_data.gender = gender
        edit_data.save()
        return redirect("/")
    dta = People.objects.get(id=id)
    context = {"dta" : dta}
    return render(request,"edit.html",context)


def aboutpage(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "about.html", context)


def blogpage(request):
    return render(request, "blog.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "about.html")
