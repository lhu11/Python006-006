from django.shortcuts import render,redirect
from django.http import  HttpResponse
# Create your views here.
def  index(request):
    return HttpResponse("Hello Django")

def myyear(request,year):
    return render(request,'html/yearview.html')

def year(request,year):
    return  HttpResponse(year)

def name(request,**kwargs):
    return HttpResponse(kwargs['name'])
def years(request,year):
    return redirect('/2020.html')