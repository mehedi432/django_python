from django.db import models

class Cardigan(models.Model):
    style = models.CharField(max_length=89)
    description = models.CharField(max_length=144)
    price = models.PositiveIntegerField()
