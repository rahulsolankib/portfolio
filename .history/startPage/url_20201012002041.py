from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
]
