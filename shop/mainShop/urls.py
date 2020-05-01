from django.urls import path

from mainShop import views


app_name = 'mainShop'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<slug>/',
         views.shoes_detail_view,
         name='shoes'),
    path('<shoes_id>/buy', views.buy, name='buy'),
    path('<shoes_id>/userorder', views.userOrderView, name='userOrder'),
]
