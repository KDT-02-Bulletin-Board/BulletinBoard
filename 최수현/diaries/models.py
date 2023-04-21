from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_diaries')
    title = models.CharField(max_length=50)

    MOODS = [
        ('매우 좋음', 1),
        ('좋음', 2),
        ('보통', 3),
        ('슬픔', 4),
        ('화남', 5),
    ]

    mood = models.CharField(max_length=10, choices=MOODS)

    def transform_mood(self):
        today_mood = self.mood.value
        if today_mood == 1:
            return '&#xF59D; ' * 3
        if today_mood == 2:
            return '&#xF59D; ' * 2 + '&#xF59E;'
        if today_mood == 3:
            return '&#xF59D; ' + '&#xF59E; ' * 2
        if today_mood == 4:
            return '&#xF2B3;'
        if today_mood == 5:
            return '&#xF46E;'

    def articles_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'
    
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(time.seconds // 60) + '분 전'
        elif time < timedelta(days=1):
            return str(time.seconds // 3600) + '시간 전'
        elif time < timedelta(weeks=1):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
        

class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_string(self):
        time = datetime.now() - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(time.seconds // 60) + '분 전'
        elif time < timedelta(days=1):
            return str(time.seconds // 3600) + '시간 전'
        elif time < timedelta(weeks=1):
            return str(time.days) + '일 전'
        else:
            return False