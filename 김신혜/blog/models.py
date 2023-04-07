from django.db import models
# 파이썬 os모듈
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정
    
    # __str__()함수 선언
    def __str__(self):
        # __str__()의 괄호 안에 들어오는 (매개변수)의 pk, title을 출력
        return f'[{self.pk}]{self.title}'
    
    # 각 레코드(filed모음)
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # 파일 경로는 제외하고 파일명만 나오게 하는 함수 생성
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    # 확장자를 찾아내는 함수도 함께 생성
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    