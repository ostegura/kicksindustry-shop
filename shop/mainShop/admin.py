from django.contrib import admin
from mainShop.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model',
                    'is_active', 'size', 'sale_cnt', )
    list_filter = ['add_date', 'name', 'is_active']
    search_fields = ['name']


@admin.register(ShoesGallery)
class ShoesGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoesImage)
class ShoesImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelSizeList)
class ModelSizeListAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoesSize)
class ShoesSizeAdmin(admin.ModelAdmin):
    pass
