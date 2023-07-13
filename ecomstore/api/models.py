from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Cloths(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='cloths', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True)
    image_url = models.URLField(max_length=2083)
    cloths_available = models.BooleanField()

    def __str__(self):
        return self.title

