from django.shortcuts import render,get_object_or_404
from .models import subject,subjectType,subjectPackage

# Create your views here.

Navbar = subjectType.objects.all().values("type_name")

def index(request):
    context = {}
    context['packageInfos'] = subjectPackage.objects.all()
    context['subjectType'] = Navbar
    return render(request,'index.html',context)

def selectSubjects(request,subject_id):
    subjectObject = get_object_or_404(subject,pk=subject_id)
    return render(request,"subject.html",context={"subjectObject":subjectObject,"subjectType":Navbar})

def baseNavbar(request):
    return render(request,"base.html",context={"subjectType":Navbar})

def typeDisplay(request,type):
    typefilter = subject.objects.filter(subject_type__type_name=type)

    return render(request,"type.html",context={"subjec_type":typefilter,"subjectType":Navbar})