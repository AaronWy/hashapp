from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("unhash",views.unhash, name="unhash")
]
