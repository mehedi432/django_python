from django.db import models


class Lead(models.Model):

    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'NewsLetter'),
    )

    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=89)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"
