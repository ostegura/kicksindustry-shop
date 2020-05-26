from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

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


class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])],)
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    price = models.CharField(default='0$', max_length=64)
    size = models.CharField(max_length=2, default='36')
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


""" Start of gallery """


class ShoesGallery(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'ShoesGallery'
        verbose_name_plural = 'ShoesGalleries'

    def __str__(self):
        return f'{self.shoes.model}'


class ShoesImage(models.Model):
    shoes_gallery = models.ForeignKey(ShoesGallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes_detail', validators=[
                              FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])

    class Meta:
        verbose_name = "ShoesImage"
        verbose_name_plural = "ShoesImages"


""" End of gallery """


""" Start of size-list"""


class ModelSizeList(models.Model):
    shoes = models.OneToOneField(Shoes,
                                 on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'ModelSizeList'
        verbose_name_plural = 'ModelSizeList'

    def __str__(self):
        return f'{self.shoes.name}  {self.shoes.model}'


class ShoesSize(models.Model):
    shoes_size = models.ForeignKey(ModelSizeList, on_delete=models.CASCADE)
    model_size = models.CharField(max_length=2, default='36')

    class Meta:
        verbose_name = "ShoesSize"
        verbose_name_plural = "ShoesSize"

    def __str__(self):
        return f'{self.model_size}'


""" End of model size list """
