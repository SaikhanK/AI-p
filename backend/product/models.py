from django.db import models

class Product(models.Model):
    title = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class productImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="product/")