from django import forms


class GetUserContactForm(forms.Form):
    user_email = forms.EmailField(required=True)
    user_name = forms.CharField(required=True)
