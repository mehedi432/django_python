from django.db import models


# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=55)
    image = models.ImageField(default='default.jpg', upload_to='category')

    def __str__(self):
        return f"{self.name}"


class Cardigan(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="cardigan")
    style = models.CharField(max_length=144)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category")
    description = models.CharField(max_length=233, blank=True)
    composition = models.CharField(max_length=64, blank=True)
    gauge = models.CharField(max_length=32, blank=True)
    size = models.CharField(max_length=32, blank=True)
    weight = models.CharField(max_length=32, blank=True)
    moq = models.CharField(max_length=32, blank=True)
    fob = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.style} is in {self.category}"


class Pullover(models.Model):
    style = models.CharField(max_length=144)
    image = models.ImageField(default="default.jpg", upload_to="pullover")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="pullover")
    description = models.CharField(max_length=233, blank=True)
    composition = models.CharField(max_length=64, blank=True)
    gauge = models.CharField(max_length=32, blank=True)
    size = models.CharField(max_length=32, blank=True)
    weight = models.CharField(max_length=32, blank=True)
    moq = models.CharField(max_length=32, blank=True)
    fob = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.style} is in {self.category}"


class Vest(models.Model):
    style = models.CharField(max_length=144)
    image = models.ImageField(default="default.jpg", upload_to="vest")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vest")
    description = models.CharField(max_length=233, blank=True)
    composition = models.CharField(max_length=64, blank=True)
    gauge = models.CharField(max_length=32, blank=True)
    size = models.CharField(max_length=32, blank=True)
    weight = models.CharField(max_length=32, blank=True)
    moq = models.CharField(max_length=32, blank=True)
    fob = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.style} is in {self.category}"
