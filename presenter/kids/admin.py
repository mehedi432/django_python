from django.contrib import admin
from .models import Category, Cardigan, Pullover, Vest

# Register your models here.
admin.site.register(Category)
admin.site.register(Cardigan)
admin.site.register(Pullover)
admin.site.register(Vest)
