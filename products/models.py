from django.db import models
from stores.models import Store


class Section(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)