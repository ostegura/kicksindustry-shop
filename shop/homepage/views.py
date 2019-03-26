from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):
    return render(request, 'homepage/welcome_text.html')


def contact(request):
    return render(request, 'homepage/contacts.html',
                  {'values': ['(099) 099-99-99 - Sasha',
                              '(088) 088-88-88 - Dasha',
                              '(077) 077-77-77 - Natasha'],
                   'mail_values': ['whatagreatemail@gmail.com',
                                   'whatagreatemail321@gmail.com']})
