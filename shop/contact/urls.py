from django.urls import path

from contact import views


app_name = 'contact'
urlpatterns = [
    path('', views.emailView, name='contacts'),
    path('members/', views.MemberView.as_view(), name='members'),
]
