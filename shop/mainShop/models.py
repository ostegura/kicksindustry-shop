from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    sex = models.CharField(max_length=64, default='unisex')
    image = models.ImageField(default='', upload_to='category', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])])
    size_table = models.ImageField(upload_to='size_table', validators=[
        FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],
        default='noimage.jpg')
    # slug = models.SlugField(unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = '.Бренд'
        verbose_name_plural = '.Бренды'

    def __str__(self):
        return f'{self.name} {self.sex}'

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],)
    articul = models.CharField(max_length=64, default='')
    model = models.CharField(max_length=128)
    price = models.FloatField(default='1.0')
    discount = models.BooleanField(default=False)
    price_after_discount = models.FloatField(default='0.0', blank=True)
    description = models.TextField(default='')
    is_active = models.BooleanField()
    quantity = models.PositiveIntegerField(default=0)
    sale_cnt = models.PositiveIntegerField(default=0)
    add_date = models.DateTimeField(verbose_name='added date', auto_now=True)
    # slug = models.SlugField(unique=True)
    slug = AutoSlugField(populate_from='model', unique=True)

    class Meta:
        verbose_name = '.Модель'
        verbose_name_plural = '.Модель'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('shoes-detail', kwargs={'slug': self.slug})


""" Start of gallery """


class ShoesGallery(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = '.Галерея'
        verbose_name_plural = '.Галереи'

    def __str__(self):
        return f'Артикул: {self.shoes.articul}, пара: {self.shoes.category.name}  {self.shoes.model}'


class ShoesImage(models.Model):
    shoes_gallery = models.ForeignKey(ShoesGallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes_detail', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],
                              default='noimage.jpg')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self):
        return f'Артикул: {self.shoes_gallery.shoes.articul}, пара:{self.shoes_gallery.shoes.category.name} {self.shoes_gallery.shoes.model}'


""" End of gallery """


""" Start of size-list"""


class ModelSizeList(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = '.Размеры'
        verbose_name_plural = '.Размеры'

    def __str__(self):
        return f'Артикул: {self.shoes.articul}, пара: {self.shoes.category.name}  {self.shoes.model}'


class ShoesSize(models.Model):
    shoes_size = models.ForeignKey(ModelSizeList, on_delete=models.CASCADE)
    model_size = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размер"

    def __str__(self):
        return f'Артикул: {self.shoes_size.shoes.articul}, размер: {self.model_size}, пара: {self.shoes_size.shoes.category.name} {self.shoes_size.shoes.model}'


""" End of model size list """
