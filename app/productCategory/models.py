from django.db import models
from ..product import *
from ..category import *

class product_category(models.Model):
    product = models.ForeignKey(Products, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.category}"
