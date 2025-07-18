from django.contrib import admin

# Register your models here.
from Product.models import product

admin.site.register(product)