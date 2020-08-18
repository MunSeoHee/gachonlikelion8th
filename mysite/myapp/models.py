from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50, blank=False)
    passwd = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class board(models.Model):
    name = models.CharField(max_length=50,blank=False)
    date = models.CharField(max_length=50, blank=False)
    memo = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name