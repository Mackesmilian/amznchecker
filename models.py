from django.db import models


class Product(models.Model):
    link = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    date_added = models.DateField('date added')

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField('price date')
    price = models.IntegerField(default=0)

    def __int__(self):
        return self.price
