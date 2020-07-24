from django.db import models

# Create your models here.
class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name