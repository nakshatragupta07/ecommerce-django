from django.db import models

# Create your models here.

CATEGORY_CHOICE = [
    ("Men","men"),
    ("Women","women"),
    ("Featured","featured"),
    ("Latest","latest")
]

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=20)
    cateogry = models.CharField(max_length=20,choices = CATEGORY_CHOICE)
    image = models.ImageField(upload_to='media')