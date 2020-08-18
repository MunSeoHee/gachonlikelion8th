from django.db import models

# Create your models here.
class Category(models.Model):
    level_nm = models.CharField(max_length=1000) #난이도 #레시피기본정보
    calorie = models.CharField(max_length=1000)  #칼로리 #레시피기본정보
    nation_nm = models.CharField(max_length=1000) #유형분류 #레시피기본정보
    cooking_time = models.CharField(max_length=1000) #조리시간 #레시피기본정보


class Detail(models.Model):
    recipe_nm_ko = models.CharField(max_length=1000) #레시피 이름 #레시피기본정보
    cooking_dc = models.CharField(max_length=100000) #요리설명 #레시피과정정보
    irdnt_nm = models.CharField(max_length=10000) #재료명 #레시피재료정보
    stre_step_image_url = models.CharField(max_length=100000) #과정 이미지 URL #레시피과정정보


