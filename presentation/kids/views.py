from django.shortcuts import render
from .models import Category, Cardigan


# Create your views here.
def index(request):
    category = Category.objects.all()
    return render(request, 'kids/index.html', {
        "categories": category
    })


def details(request, category_id):
    category = Category.objects.get(pk=category_id)
    cardigans = Cardigan.objects.all()

    return render(request, "kids/details.html", {
        "category": category, 
        "cardigans": cardigans
    })