from django.contrib import admin
from .models import RiskModel
# Register your models here.

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('name', 'phone')})
admin.site.register(RiskModel)
