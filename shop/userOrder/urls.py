from django.urls import path

from .views import UserOrderView


app_name = 'userOrder'
urlpatterns = [
    path('<int:id>/', UserOrderView, name='order'),
]
