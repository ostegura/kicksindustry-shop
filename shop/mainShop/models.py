from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.core.validators import MinLengthValidator, int_list_validator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(default='', upload_to='category', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

# class CommonInfo(models.Model):
#   # fields

#   # inherit this class to get it's fields

#     class Meta:
#         abstract = True


class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    price = models.CharField(default='0$', max_length=64)
    size = models.PositiveIntegerField()
    description = models.TextField(default='')
    is_active = models.BooleanField()
    sale_cnt = models.PositiveIntegerField(default=0)
    add_date = models.DateTimeField(verbose_name='added date', auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Shoes'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('shoes-detail', kwargs={'slug': self.slug})


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
