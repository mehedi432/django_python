from django.contrib import admin
from .models import Category, Cardigan, Vest, Pullover


# Register your models here.
admin.site.register(Category)
admin.site.register(Cardigan)
admin.site.register(Vest)
admin.site.register(Pullover)
