from django.shortcuts import render, get_object_or_404
# from django.views import generic
# from django.http import HttpResponseRedirect

from .forms import UserOrderForm
from .models import UserOrder
from mainShop.models import Shoes
# Create your views here.


def UserOrderView(request, id):
    # print('1')
    shoes = get_object_or_404(Shoes, id=id)
    if request.method == 'POST':
        # print('2')
        user_order = UserOrderForm(request.POST)
        if user_order.is_valid():
            # print('3')
            name = user_order.cleaned_data['name']
            surname = user_order.cleaned_data['surname']
            address = user_order.cleaned_data['address']
            from_email = user_order.cleaned_data['from_email']
            phone = user_order.cleaned_data['phone']
            # print('4')
            UserOrder.objects.create(name=name,
                                     surname=surname,
                                     address=address,
                                     phone_no=phone,
                                     email=from_email,
                                     shoes_name=shoes.name,
                                     model=shoes.model,
                                     size=shoes.size
                                     )
            # print('5')
            return render(request, 'userOrder/success.html',
                          {'shoes': shoes})
        else:
            # print(user_order.errors)
            error_message = 'Please, fill fields correctly!'
            return render(request, 'userOrder/user_order.html',
                          {'form': user_order, 'error': error_message})
    else:
        # print('6')
        user_order = UserOrderForm()
    # print('7')
    return render(request, 'userOrder/user_order.html',
                  {'form': user_order})
