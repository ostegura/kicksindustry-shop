from django.urls import path

from mainShop import views


app_name = 'mainShop'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('<int:pk>/', views.ShoesListView.as_view(), name='detail'),
    path('<pk>/shoes',
         views.ShoesDetailView.as_view(),
         name='shoes'),
]
