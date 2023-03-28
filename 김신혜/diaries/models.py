from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()