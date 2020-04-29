from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.http import HttpResponseRedirect
# from django.urls import reverse


from mainShop.models import Category, Shoes


class MenuView(generic.ListView):
    template_name = 'mainShop/menu.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Category.objects.all().order_by("name")[:10]


class DetailView(generic.DetailView):
    model = Category
    template_name = 'mainShop/detail.html'

    def get_queryset(self):
        return Category.objects.all()


def shoes_detail_view(request, slug):
    shoes_slug = get_object_or_404(Shoes, slug=slug)
    return render(request, 'mainShop/shoes.html', {'shoes': shoes_slug, })


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
        return render(request, 'mainShop/success.html',
                      {'shoes': shoes, })
