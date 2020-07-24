from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=400)

    class Meta:
        db_table = 'users_info'

def _str_(self):
    return self.title
    