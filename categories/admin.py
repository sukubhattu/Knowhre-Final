from django.contrib import admin
from .models import Category, Company
# from .models import Company, Product
# # Register your models here.
admin.site.register(Category)
admin.site.register(Company)
