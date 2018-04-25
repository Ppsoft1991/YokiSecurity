from django.shortcuts import render
from .models import subject,subjectPackage

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
    print(package_name+'--------[][]')
    packageFilter = subject.objects.filter(subjectpackage__package_name=package_name)
    print("-----------",packageFilter)
    return render(request,'package.html',context={"package_info":packageFilter})