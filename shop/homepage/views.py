from django.shortcuts import render
from django.views import generic

from mainShop.models import Category
from .models import UserForMailing
from .forms import GetUserContactForm


def index(request):
    return render(request, 'homepage/welcome_text.html')


def mailingView(request):
    if request.method == 'POST':
        user = GetUserContactForm(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            email = user.cleaned_data['email']
            UserForMailing.objects.create(name=name, email=email)
            return render(request, 'homepage/mailing_success.html')
        else:
            error_message = 'Please, fill fields correctly!'
            return render(request, 'homepage/mailing.html',
                          {'form': user,
                           'error': error_message,
                           })
    else:
        user = GetUserContactForm()
    return render(request, 'homepage/mailing.html', {'form': user})
