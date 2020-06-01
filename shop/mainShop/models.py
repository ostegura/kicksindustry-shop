from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    sex = models.CharField(max_length=64, default='unisex')
    image = models.ImageField(default='', upload_to='category', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])])
    size_table = models.ImageField(upload_to='size_table', validators=[
        FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],
        default='noimage.jpg')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирма'

    def __str__(self):
        return f'{self.name} {self.sex}'

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],)
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    price = models.CharField(max_length=64, default='1$')
    discount = models.BooleanField(default=False)
    price_after_discount = models.CharField(max_length=64, default='0$', blank=True)
    description = models.TextField(default='')
    is_active = models.BooleanField()
    sale_cnt = models.PositiveIntegerField(default=0)
    add_date = models.DateTimeField(verbose_name='added date', auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('shoes-detail', kwargs={'slug': self.slug})


""" Start of gallery """


class ShoesGallery(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    def __str__(self):
        return f'{self.shoes.model}'


class ShoesImage(models.Model):
    shoes_gallery = models.ForeignKey(ShoesGallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes_detail', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])],
                              default='noimage.jpg')

    class Meta:
        verbose_name = "Фото обуви"
        verbose_name_plural = "Фото обуви"

    def __str__(self):
        return f'{self.shoes_gallery.shoes.name} {self.shoes_gallery.shoes.model}'


""" End of gallery """


""" Start of size-list"""


class ModelSizeList(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Ключ на размеры для модели'
        verbose_name_plural = 'Ключ на размеры для модели'

    def __str__(self):
        return f'{self.shoes.name}  {self.shoes.model}'


class ShoesSize(models.Model):
    shoes_size = models.ForeignKey(ModelSizeList, on_delete=models.CASCADE)
    model_size = models.CharField(max_length=2, default='36')

    class Meta:
        verbose_name = "Доступные размеры"
        verbose_name_plural = "Доступные размеры"

    def __str__(self):
        return f'Size: {self.model_size}, {self.shoes_size.shoes.name} {self.shoes_size.shoes.model}'


""" End of model size list """
