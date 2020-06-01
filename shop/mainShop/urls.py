from django.urls import path

from mainShop import views


app_name = 'mainShop'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('male/', views.MaleListView.as_view(), name='male'),
    path('female/', views.FemaleListView.as_view(), name='female'),
    path('<int:id>/', views.detailView, name='detail'),
    path('<slug>/',
         views.shoes_detail_view,
         name='shoes'),
    path('<shoes_id>/buy', views.buy, name='buy'),
]
