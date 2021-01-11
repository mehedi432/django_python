from django.db import models


# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name}"


class Gender(models.Model):
    title = models.CharField(max_length=21)

    def __str__(self):
        return f"{self.title}"


class Cardigan(models.Model):
    style = models.CharField(max_length=144)
    name = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    composition = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.style} is in {self.name}"
