from django.db import models


class UserForMailing(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(blank=True)

    def __str__(self):
        return "{} {}".format(self.email, self.name)
