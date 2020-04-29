from django.db import models
from django.core.validators import FileExtensionValidator


class TeamMember(models.Model):
    image = models.ImageField(upload_to='teamMembers',
                              blank=True, null=True, verbose_name='Image',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'], 
                                                                 message='only png, jpg, jpeg extensions')]
                              )
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    number = models.CharField(max_length=25)
    status = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
