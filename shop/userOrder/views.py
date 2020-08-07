from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
# from django.views import generic
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .forms import UserOrderForm
from .models import UserOrder
from shop import settings
from mainShop.models import Shoes, ShoesSize

from liqpay import LiqPay

from django.views.generic import TemplateView, View
from django.shortcuts import render
# Create your views here.


def UserOrderView(request, id):
    # print('1')
    shoes = get_object_or_404(Shoes, id=id)
    size_list = ShoesSize.objects.filter(shoes_size__shoes=shoes).order_by("model_size")
    shoes_price = shoes.price

    if request.method == 'POST':
        # print('2')
        user_order = UserOrderForm(request.POST)
        if user_order.is_valid():
            # print('3')
            name = user_order.cleaned_data['name']
            surname = user_order.cleaned_data['surname']
            size = user_order.cleaned_data['size']
            address = user_order.cleaned_data['address']
            from_email = user_order.cleaned_data['from_email']
            phone = user_order.cleaned_data['phone']
            # print('4')
            UserOrder.objects.create(name=name,
                                     surname=surname,
                                     address=address,
                                     phone_no=phone,
                                     email=from_email,
                                     shoes_name=shoes.category.name,
                                     model=shoes.model,
                                     size=size
                                     )
            # print('5')
            try:
                # send_mail(f'{shoes.category.name} {shoes.model}',
                #           f'\
                #             Client: {name} {surname};\n \
                #             Product: {shoes.category.name} {shoes.model} - {size};\n \
                #             Address: {address};\n \
                #             E-mail: {from_email};\n \
                #             Phone: {phone}',
                #           from_email,
                #           ['stegura99@gmail.com'])
                shoes.sale_cnt += 1
                shoes.save()
            except BadHeaderError:
                return HttpResponse('Проблема с отправкой отчета о покупке.')
            # return render(request, 'userOrder/success.html',
            #               {'shoes': shoes,
            #                'size': size})
            return redirect('userOrder:pay_view', price=shoes_price)
        else:
            # print(user_order.errors)
            error_message = 'Пожалуйста, заполните поля правильно.'
            return render(request, 'userOrder/user_order.html',
                          {'form': user_order,
                           'error': error_message,
                           'size_list': size_list
                           })
    else:
        # print('6')
        user_order = UserOrderForm()
    # print('7')
    return render(request, 'userOrder/user_order.html',
                  {'form': user_order,
                   'size_list': size_list})


class PayView(TemplateView):
    template_name = 'userOrder/pay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': self.kwargs['price'],
            # 'amount': '0.01',
            'currency': 'UAH',
            'description': 'Оплата обуви, отправка с магазина Kicks Industry, г. Ужгород, ул. Льва Толстого, 5',
            'order_id': 'order_id_1',
            'version': '3',
            'sandbox': 0, # sandbox mode, set to 1 to enable it
            'server_url': 'https://test.com/billing/pay-callback/', # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})

@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()