from django import forms


class GetUserContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=64)
    email = forms.EmailField(required=True)
