from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="Start-Page"),
    path('about/', views.about,name="About-Page"),
    path('material/', views.material,name="Material"),
    path('silver/', views.silver,name="Silver")    
]
