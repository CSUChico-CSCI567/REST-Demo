from django.db import models

# Create your models here.
class FoodModel(models.Model):
    url = models.URLField(max_length = 240) 
    photo_url = models.URLField(max_length = 240)
    title = models.CharField(max_length=240)

    def __str__(self):
        return self.url + " " + self.photo_url + " " + self.title