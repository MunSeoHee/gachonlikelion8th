from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()

    def __str__(self):
            return self.title