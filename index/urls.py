from django.urls import path
from .views import selectSubjects,typeDisplay

urlpatterns = [
    path('/<int:subject_id>',selectSubjects,name="subject_id"),
    path('/<type>',typeDisplay,name="type"),
]