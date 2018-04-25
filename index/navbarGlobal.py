from .models import subjectType
def navbar(request):
    Navbar = subjectType.objects.all().values("type_name")
    return {"navbar":Navbar}