from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('name', 'phone')})
admin.site.register(User, UserAdmin)
