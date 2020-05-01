from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import BadHeaderError
# from django.urls import reverse
from django.shortcuts import redirect

from mainShop.models import Category, Shoes, UserOrder
from mainShop.forms import UserOrderForm


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
    # TO DO: redirect to user order view and store data about user


def userOrderView(request, id):
    if request.method == 'GET':
        form = UserOrderForm()
    else:
        form = UserOrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            address = form.cleaned_data['address']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            try:
                userOrder = UserOrder.objects.create(name=name,
                                                     surname=surname,
                                                     address=address,
                                                     phone_no=phone,
                                                     email=from_email,
                                                     )
                userOrder.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "mainShop/success.html")
    return render(request, "mainShop/user_order.html", {'form': form})
