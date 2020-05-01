from django import forms
from django.core.validators import MinLengthValidator, int_list_validator


class UserOrderForm(forms.Form):
    name = forms.CharField(max_length=64, required=True)
    surname = forms.CharField(max_length=64, required=True)
    address = forms.CharField(max_length=128, required=True)
    from_email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10,
                            validators=[int_list_validator(sep=''),
                                        MinLengthValidator(10), ],)
