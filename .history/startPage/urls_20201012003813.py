from django.urls import path
from . import views

urlpatterns = [
    path('startPage/', views.home,name="Start-Page"),
    path('about/', views.about,name="About-Page"),
]
