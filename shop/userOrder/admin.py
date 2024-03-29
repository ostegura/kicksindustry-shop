from django.contrib import admin

from .models import UserOrder

# Register your models here.


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "shoes_name",
                    "model", "size", "address", "time", "mod_check")
