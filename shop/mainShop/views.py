from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views import generic


from mainShop.models import Category, Shoes


class MenuView(generic.ListView):
    template_name = 'mainShop/menu.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Category.objects.all().order_by("name")[:5]


class ShoesListView(generic.ListView):
    template_name = 'mainShop/detail.html'
    context_object_name = 'detail_list'

    def get_queryset(self):
        return Shoes.objects.all().order_by("name")[:5]


class ShoesDetailView(generic.DetailView):
    model = Category
    template_name = 'mainShop/shoes.html'
