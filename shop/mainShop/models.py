from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# class CommonInfo(models.Model):
#   # fields

#   # inherit this class to get it's fields

#     class Meta:
#         abstract = True


class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoes')
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    size = models.PositiveIntegerField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'Shoes'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.model
