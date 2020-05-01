from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import UserOrderForm
from .models import UserOrder
# Create your views here.

# def userOrderView(request, id):
#     if request.method == 'GET':
#         form = UserOrderForm()
#     else:
#         form = UserOrderForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             surname = form.cleaned_data['surname']
#             address = form.cleaned_data['address']
#             from_email = form.cleaned_data['from_email']
#             phone = form.cleaned_data['phone']
#             try:
#                 userOrder = UserOrder.objects.create(name=name,
#                                                      surname=surname,
#                                                      address=address,
#                                                      phone_no=phone,
#                                                      email=from_email,
#                                                      )
#                 userOrder.save()
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return render(request, "mainShop/success.html")
#     return render(request, "mainShop/user_order.html", {'form': form})


class UserOrderView(generic.TemplateView):
    template_name = 'mainShop/user_order.html'

    def post(self, request, *args):
        user_order = UserOrderForm(request.POST)
        if user_order.is_valid():
            name = user_order.cleaned_data['name']
            surname = user_order.cleaned_data['surname']
            address = user_order.cleaned_data['address']
            from_email = user_order.cleaned_data['from_email']
            phone = user_order.cleaned_data['phone']
            userOrder = UserOrder.objects.create(name=name,
                                                 surname=surname,
                                                 address=address,
                                                 phone_no=phone,
                                                 email=from_email,
                                                 )
            userOrder.save()
        return HttpResponseRedirect(reverse('user_order'))
