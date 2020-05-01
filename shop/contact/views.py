from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from contact.models import TeamMember

from contact.forms import ContactForm


class MemberView(generic.ListView):
    template_name = 'contact/member_table.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return TeamMember.objects.all().order_by("pk")[:5]


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['stegura99@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contact/success.html")
    return render(request, "contact/contacts.html", {'form': form})
