from django.contrib import admin
from mainShop.models import Category, Shoes, UserOrder


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "model",
                    "is_active", "size", "sale_cnt", )
    list_filter = ['add_date', 'name', 'is_active']
    search_fields = ['name']


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "surname",)
