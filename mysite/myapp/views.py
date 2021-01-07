from django.shortcuts import redirect
from django.http import  JsonResponse

from . import models

# Create your views here.
def index(request):
    return redirect("/food/")

def get_food(request):
    food_objects = models.FoodModel.objects.all()
    food_list = {}
    food_list["recipes"]=[]
    for food in food_objects:
        temp_food = {}
        temp_food["url"] = food.url
        temp_food["photo_url"] = food.photo_url
        temp_food["title"] = food.title
        food_list["recipes"] += [temp_food]
    return JsonResponse(food_list)
