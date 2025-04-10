from django.contrib import admin

# Register your models here.
# meu_app/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
