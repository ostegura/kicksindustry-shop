from django.urls import path

from .views import UserOrderView, PayView, PayCallbackView


app_name = 'userOrder'
urlpatterns = [
    path('<int:id>/', UserOrderView, name='order'),
    path('pay/<price>', PayView.as_view(), name='pay_view'),
    path('pay-callback/', PayCallbackView.as_view(), name='pay_callback'),
]
