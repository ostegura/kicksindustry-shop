from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.mail import BadHeaderError
# from django.urls import reverse
# from django.shortcuts import redirect

from mainShop.models import *


class MenuView(generic.ListView):
    template_name = 'mainShop/menu.html'
    context_object_name = 'menu_list'
    paginate_by = 9

    def get_queryset(self):
        return Category.objects.all().order_by("name")


def detailView(request, id):
    category = get_object_or_404(Category, id=id)
    shoes_set = category.shoes_set.all().order_by('id')

    page = request.GET.get('page', 1)

    paginator = Paginator(shoes_set, 10)
    try:
        shoes_list = paginator.page(page)
    except PageNotAnInteger:
        shoes_list = paginator.page(1)
    except EmptyPage:
        shoes_list = paginator.page(paginator.num_pages)

    return render(request, 'mainShop/detail.html', {'category': shoes_list, })


def shoes_detail_view(request, slug):
    shoes = get_object_or_404(Shoes, slug=slug)
    images = ShoesImage.objects.filter(shoes_gallery__shoes=shoes)
    sizes = ShoesSize.objects.filter(shoes_size__shoes=shoes)
    return render(request, 'mainShop/shoes.html', {'shoes': shoes,
                                                   'images': images,
                                                   'sizes': sizes, })


def buy(request, shoes_id):
    try:
        if request.method == 'POST':
            shoes = Shoes.objects.get(id=shoes_id)
    except (KeyError, Shoes.DoesNotExist):
        return render(request, 'mainShop/detail.html',
                      {'error_message': "Error! You can't buy this pair!"})
    else:
        shoes.sale_cnt += 1
        shoes.save()
        return redirect('userOrder:order', id=shoes_id)
