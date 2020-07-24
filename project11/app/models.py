
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100) #길이조정
    body = models.TextField() #길이 지정 안함
    date = models.DateTimeField(auto_now_add=True) #사용자 작성 시간 작성
    like = models.IntegerField()

    def _str_(self):
        return self.title
