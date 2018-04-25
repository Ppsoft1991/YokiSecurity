from django.urls import path
from .views import typeDisplay,packageDisplay

urlpatterns = [
    path('<type>',typeDisplay,name="type"),
]