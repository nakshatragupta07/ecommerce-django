from django.contrib import admin
from .models import Product

# Register your models here.


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  [ 'id','title','price','description','size','cateogry','image']