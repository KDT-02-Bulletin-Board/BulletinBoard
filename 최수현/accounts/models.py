from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    birthday = models.DateField(null=True, blank=True)

    def articles_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'
    
    profile_image = models.ImageField(null=True, blank=True)