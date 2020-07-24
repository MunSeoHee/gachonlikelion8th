from django.db import models

# Create your models here.
class Email(models.Model):
    address = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.address