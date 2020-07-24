from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) #title 이라는 최대 200글자 문자 데이터 생성
    pub_date = models.DateTimeField('data published') # pub_date라는 날짜 시간 데이터 저장
    body = models.TextField() # body 라는 줄글 문자 저장

    # 이 객체를 가르키는 말을 title이라 정하겠다.
    def __str__(self): 
        return self.title
