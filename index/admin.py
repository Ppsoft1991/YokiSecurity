from django.contrib import admin
from .models import subject,subjectType,subjectPackage

# Register your models here.
class subjectAdmin(admin.ModelAdmin):
    list_display = ("title","author","flag","answer_number","last_answer_time")

admin.site.register(subject,subjectAdmin)
admin.site.register(subjectType)
admin.site.register(subjectPackage)