from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django_filters.views import FilterView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q

from .filters import ShoesFilter
from .models import *


class MaleListView(generic.ListView):
    model = Shoes
    template_name = 'mainShop/male.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['male_list'] = Category.objects.filter(sex='men').order_by("name")
        context['title'] = 'Мужские кроссовки - Kicks Industry'
        context['description'] = 'Мужские оригинальные кроссовки в интернет-магазине ➦Kicks Industry. ☎: (099) 743-68-85. Мужские кроссовки, $ лучшие цены, ✈ быстрая доставка, ☑ гарантия!' \
                                 '₴ Скидочные сертификаты'
        context['keywords'] = 'Купить кроссовки, купить мужскую обувь, дешево, Adidas, Nike, Reebok, ' \
                              'адидас, найк, рибок, Украина, Ужгород, Киев, Харьков, Одесса, Львов'
        return context


class FemaleListView(generic.ListView):
    model = Shoes
    template_name = 'mainShop/female.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['female_list'] = Category.objects.filter(sex='women').order_by("name")
        context['title'] = 'Женские кроссовки - Kicks Industry'
        context['description'] = 'Женские оригинальные кроссовки в интернет-магазине ➦Kicks Industry. ☎: (099) 743-68-85. Женские кроссовки, $ лучшие цены, ✈ быстрая доставка!' \
                             '₴ Скидочные сертификаты'
        context['keywords'] = 'Купить кроссовки, купить женскую обувь, дешево, Adidas, Nike, Reebok,' \
                              'адидас, найк, рибок, Украина, Ужгород, Киев, Харьков, Одесса, Львов'
        return context


class ReturnAndExchangeView(generic.TemplateView):
    template_name = 'mainShop/return_and_exchange.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Возврат и обмен - Kicks Industry'
        context['description'] = 'Обмен и возврат на протяжении 14 дней в интернет-магазине ➦Kicks Industry. ☎: (099) 743-68-85.'
        context['keywords'] = 'Возврат кроссовок, обмен кроссовок, гарантия, Киев, Ужгород, Киев, Харьков, Одесса, Львов'
        return context

# start of menu detail view (example: nike (male) -> nike shoes)

class ModelFilteredListView(FilterView):
    filterset_class = ShoesFilter
    template_name = 'mainShop/detail.html'
    paginate_by = 24
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['title'] = f"Кроссовки {category.name} - Kicks Industry"
        context['description'] = 'Мужские и женские оригинальные кроссовки в интернет-магазине ➦Kicks Industry. ☎: (099) 743-68-85. ' \
                                 'Мужские и женские кроссовки, $ лучшие цены, ✈ быстрая доставка!' \
                                 '₴ Скидочные сертификаты'
        context['keywords'] = 'Купить кроссовки, купить женскую обувь, купить мужскую обувь, дешево, Adidas, Nike, Reebok,' \
                              'адидас, найк, рибок, Украина, Ужгород, Киев, Харьков, Одесса, Львов'
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Shoes.objects.filter(category=category)


# end of menu detail view (example: nike (male) -> nike shoes)

def shoes_detail_view(request, slug):
    shoes = get_object_or_404(Shoes, slug=slug)
    images = ShoesImage.objects.filter(shoes_gallery__shoes=shoes)
    sizes = ShoesSize.objects.filter(shoes_size__shoes=shoes).exclude(is_active=False).order_by("model_size")
    size_table = shoes.category.size_table
    title = f'{shoes.category.name} {shoes.model} - Kicks Industry'
    description = f'{shoes.category.name} {shoes.model} - {shoes.price}₴. Размеры: {sizes}. Мужские и женские оригинальные кроссовки в интернет-магазине ➦Kicks Industry. ' \
                  '☎: (099) 743-68-85. ✈ быстрая доставка! ₴ Скидочные сертификаты'
    keywords = f'{shoes.category.name}, {shoes.model}, дешево, оригинал, Украина, Ужгород, Киев, Харьков, Одесса, Львов'
    return render(request, 'mainShop/shoes.html', {'shoes': shoes,
                                                   'images': images,
                                                   'sizes': sizes,
                                                   'size_table': size_table,
                                                   'description': description,
                                                   'keywords': keywords,
                                                   'title': title})
