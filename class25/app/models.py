from django.db import models

# Create your models here.
class list(models.Model):
    price = models.IntegerField()
    product = models.CharField(max_length=100)
    num = models.IntegerField()
    check = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    


