from django.contrib import admin

from .models.category import Category
from .models.page import Page

admin.site.register(Category)
admin.site.register(Page)
