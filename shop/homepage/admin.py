from django.contrib import admin
from .models import UserForMailing

# Register your models here.
@admin.register(UserForMailing)
class UserForMailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    list_filter = ['name', 'email']
    list_per_page = 50
