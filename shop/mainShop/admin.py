from django.contrib import admin
from mainShop.models import *


class ShoesInline(admin.StackedInline):
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


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'articul', 'model',
                    'is_active', 'sale_cnt', 'discount', 'quantity')
    list_filter = ['add_date', 'name', 'is_active', 'discount', 'quantity']
    list_per_page = 50
    search_fields = ['name', 'articul']
    # inlines = [
    #     ShoesSizeListInline, ShoesImageInline,
    # ]


@admin.register(ShoesGallery)
class ShoesGalleryAdmin(admin.ModelAdmin):
    search_fields = ['shoes__articul', 'shoes__name', 'shoes__model']
    list_filter = ['shoes']
    list_per_page = 50
    inlines = [
        ShoesImageInline,
    ]


@admin.register(ShoesImage)
class ShoesImageAdmin(admin.ModelAdmin):
    list_per_page = 50


@admin.register(ModelSizeList)
class ModelSizeListAdmin(admin.ModelAdmin):
    search_fields = ['shoes__articul', 'shoes__name', 'shoes__model']
    list_filter = ['shoes']
    list_per_page = 50
    inlines = [
        ShoesSizeListInline,
    ]


@admin.register(ShoesSize)
class ShoesSizeAdmin(admin.ModelAdmin):
    search_fields = ['model_size', 'shoes_size__shoes__articul']
    list_per_page = 50
