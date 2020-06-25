from django.contrib import admin
from mainShop.models import *


class ShoesInline(admin.TabularInline):
    model = Shoes
    extra = 0


class ShoesImageInline(admin.StackedInline):
    model = ShoesImage
    extra = 0


class ShoesSizeListInline(admin.StackedInline):
    model = ShoesSize
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex',)
    search_fields = ['name', 'sex']
    list_filter = ['name', 'sex']
    list_per_page = 30
    inlines = [
        ShoesInline,
    ]


@admin.register(ShoesGallery)
class ShoesGalleryAdmin(admin.ModelAdmin):
    search_fields = ['shoes__articul', 'shoes__category__name', 'shoes__model']
    list_filter = ['shoes__model', 'shoes__category__name']
    list_per_page = 50
    inlines = [
        ShoesImageInline,
    ]


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('category', 'articul', 'model',
                    'is_active', 'sale_cnt', 'discount', 'quantity')
    list_filter = ['add_date', 'is_active', 'discount', 'quantity']
    list_per_page = 50
    search_fields = ['shoes__category__name', 'articul']


@admin.register(ShoesImage)
class ShoesImageAdmin(admin.ModelAdmin):
    list_per_page = 50


@admin.register(ModelSizeList)
class ModelSizeListAdmin(admin.ModelAdmin):
    search_fields = ['shoes__articul', 'shoes__category__name', 'shoes__model']
    list_filter = ['shoes__model', 'shoes__category__name']
    list_per_page = 50
    inlines = [
        ShoesSizeListInline,
    ]


@admin.register(ShoesSize)
class ShoesSizeAdmin(admin.ModelAdmin):
    search_fields = ['model_size', 'shoes_size__shoes__articul']
    list_per_page = 50
