from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('name', 'phone')})
admin.site.register(User,UserAdmin)
