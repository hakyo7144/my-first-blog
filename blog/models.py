'''
모델작업
2019-12-12
'''
# from 또는 import는 다른 파일의 기능을 가져다 사용하기 위해 사용하기 전에 먼저 선언한다.
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
