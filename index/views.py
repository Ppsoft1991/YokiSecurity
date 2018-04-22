from django.shortcuts import render,get_object_or_404
from .models import subject,subjectType,subjectPackage

# Create your views here.
def index(request):
    context = {}
    context['packageInfos'] = subjectPackage.objects.all()
    print(f"------------{context}-----------")
    return render(request,'index.html',context)

def selectSubjects(request,subject_id):
    subjectObject = get_object_or_404(subject,pk=subject_id)
    return render(request,"subject.html",context={"subjectObject":subjectObject})