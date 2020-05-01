from django.urls import path

from .views import UserOrderView


app_name = 'userOrder'
urlpatterns = [
    path('', UserOrderView.as_view(), name='user_order'),
]
