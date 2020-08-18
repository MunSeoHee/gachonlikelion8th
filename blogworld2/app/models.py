from django.db import models

# Create your models here.
class Blog(models.Model):
    CATEGORY = (
        ('Django','Django'),
        ('Python', 'Python'),
        ('html/CSS','html/CSS'),
        ('JS/JQuery','JS/JQuery'),
        )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name