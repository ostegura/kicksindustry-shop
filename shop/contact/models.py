from django.db import models


class TeamMember(models.Model):
    image = models.ImageField(upload_to='teamMembers')
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    number = models.CharField(max_length=25)
    status = models.CharField(max_length=128)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
