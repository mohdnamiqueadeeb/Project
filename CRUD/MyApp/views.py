from typing import ValuesView
from django.http import request
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from .models import Employee


def home(request):
    data = Employee.objects.all()
    return render(request, 'index.html', {"Data": data})


def addrecord(request):
    if(request.method == "POST"):
        e = Employee()
        e.name = request.POST.get('name')
        e.salary = request.POST.get('salary')
        e.designation = request.POST.get('designation')
        e.city = request.POST.get('city')
        e.state = request.POST.get('state')
        e.country = request.POST.get('country')
        e.save()
        return HttpResponseRedirect('/')
    return render(request, 'add.html')


def deleteRecord(request, num):
    data = Employee.objects.get(eid=num)
    data.delete()
    return HttpResponseRedirect('/')


def editRecord(request, num):
    data = Employee.objects.get(eid=num)
    if(request.method == "POST"):
        data.name = request.POST.get('name')
        data.salary = request.POST.get('salary')
        data.designation = request.POST.get('designation')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.country = request.POST.get('country')
        data.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {"Data": data})
