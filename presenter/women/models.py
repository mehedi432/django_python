from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=89)
    image = models.ImageField(default='default.jpg', upload_to='category')

    def __str__(self):
        return self.name


class Cardigan(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    style = models.CharField(max_length=34)

    def __str__(self):
        return self.style


class Pullover(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    style = models.CharField(max_length=34)

    def __str__(self):
        return self.style


class Vest(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    style = models.CharField(max_length=34)

    def __str__(self):
        return self.style
