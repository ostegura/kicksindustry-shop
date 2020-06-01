from django.contrib import admin
from mainShop.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex',)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model',
                    'is_active', 'sale_cnt', 'discount', )
    list_filter = ['add_date', 'name', 'is_active', 'discount']
    search_fields = ['name']


@admin.register(ShoesGallery)
class ShoesGalleryAdmin(admin.ModelAdmin):
    search_fields = ['shoes']
    list_filter = ['shoes']


@admin.register(ShoesImage)
class ShoesImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelSizeList)
class ModelSizeListAdmin(admin.ModelAdmin):
    search_fields = ['shoes']
    list_filter = ['shoes']


@admin.register(ShoesSize)
class ShoesSizeAdmin(admin.ModelAdmin):
    pass
