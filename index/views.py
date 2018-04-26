from django.shortcuts import render,get_object_or_404
from .models import subject,subjectPackage
from django.http import HttpResponse
import json
# Create your views here.

#Navbar = subjectType.objects.all().values("type_name")

def index(request):
    context = {}
    context['packageInfos'] = subjectPackage.objects.all()
    return render(request,'index.html',context,)

def typeDisplay(request,type):
    typefilter = subject.objects.filter(subject_type__type_name=type)
    return render(request,"type.html",context={"subjec_type":typefilter})

def packageDisplay(request,package_name):
    packageFilter = subject.objects.filter(subjectpackage__package_name=package_name)
    return render(request,'package.html',context={"package_info":packageFilter})

def checkFlag(request,flag):
    try:
        subject.objects.get(flag=flag)
        response = {'flag_status': 'success'}
    except:
        response = {'flag_status': 'false'}
    return HttpResponse(json.dumps(response),content_type='application/json')