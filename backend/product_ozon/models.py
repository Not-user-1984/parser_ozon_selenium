from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.CharField(max_length=50)
    image_url = models.URLField()
    code_product = models.IntegerField()

    def __str__(self):
        return self.name