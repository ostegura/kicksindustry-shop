from django.db import models


class UserForMailing(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Клиент для рассылки'
        verbose_name_plural = 'Клиенты для рассылки'

    def __str__(self):
        return "{} {}".format(self.email, self.name)
