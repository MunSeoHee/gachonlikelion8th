from django.db import models

# Create your models here.
class Blog(models.Model): # Blog 라는 이름의 객체 틀(Model) 생성
    title = models.CharField(max_length=200) # title라는 최대 200글자 문자 데이터 생성
    pub_date= models.DateTimeField('date published') #put_date 라는 시간 데이터 저장
    body = models.TextField() # body 라는 줄글 문자 생성

    # 이 객체를 가르키는 말을 title로 정하겠다.
    def __str__(self):
        return self.title
