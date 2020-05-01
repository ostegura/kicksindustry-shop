from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator
from django.urls import reverse


# Create your models here.


class UserOrder(models.Model):
    name = models.CharField(max_length=64, default='Name', blank=False)
    surname = models.CharField(max_length=64, default='Surname', blank=False)
    address = models.CharField(
        max_length=128, default='Address', blank=False)
    phone_no = models.CharField(verbose_name="Phone number", max_length=10,
                                validators=[int_list_validator(sep=''),
                                            MinLengthValidator(10), ],
                                default='1234567890')
    email = models.EmailField(
        max_length=128, default='defaultemail@django.com')
    shoes_name = models.CharField(
        max_length=64, default='Shoes name')
    model = models.CharField(max_length=128)
    size = models.CharField(max_length=2, default='')
    time = models.DateTimeField(verbose_name='order time', auto_now=True)
    mod_check = models.BooleanField(default=False)

    def __str__(self):
        return str(self.surname)

    def get_absolute_url(self):
        return reverse('userorder', kwargs={'id': self.id})
