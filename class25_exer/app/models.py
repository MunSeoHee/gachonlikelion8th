from django.db import models

# Create your models here.
class List(models.Model):
    price = models.IntegerField()
    product = models.CharField(max_length=100)
    num = models.IntegerField()
    check = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product