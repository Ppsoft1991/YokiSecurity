from django.urls import path
from .views import selectSubjects

urlpatterns = [
    path('/<int:subject_id>',selectSubjects,name="subject_id")
]