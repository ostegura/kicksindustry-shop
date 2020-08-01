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
        return context


class FemaleListView(generic.ListView):
    model = Shoes
    template_name = 'mainShop/female.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['female_list'] = Category.objects.filter(sex='women').order_by("name")
        return context


class ReturnAndExchangeView(generic.TemplateView):
    template_name = 'mainShop/return_and_exchange.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

# start of menu detail view (example: nike (male) -> nike shoes)


class ModelFilteredListView(FilterView):
    filterset_class = ShoesFilter
    template_name = 'mainShop/detail.html'
    paginate_by = 24
    ordering = 'id'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Shoes.objects.filter(category=category)


# end of menu detail view (example: nike (male) -> nike shoes)

def shoes_detail_view(request, slug):
    shoes = get_object_or_404(Shoes, slug=slug)
    images = ShoesImage.objects.filter(shoes_gallery__shoes=shoes)
    sizes = ShoesSize.objects.filter(shoes_size__shoes=shoes).exclude(is_active=False).order_by("model_size")
    size_table = shoes.category.size_table
    return render(request, 'mainShop/shoes.html', {'shoes': shoes,
                                                   'images': images,
                                                   'sizes': sizes,
                                                   'size_table': size_table})
