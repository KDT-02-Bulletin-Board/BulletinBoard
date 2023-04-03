from django.db import models
import os
from django.conf import settings

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=50)
    record_date = models.DateTimeField(null=True, blank=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    #게시글 삭제시 첨부한 파일 삭제
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        if self.imgfile:
            self.imgfile.delete()