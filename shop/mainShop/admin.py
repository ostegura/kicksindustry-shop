from django.contrib import admin
from mainShop.models import Category, Shoes

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Shoes)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "is_active", "size",)
