from django.contrib import admin

from .models import Blog

# Register your models here.
# Recupération de données pour l'afficher dans le panneau d'admin
admin.site.register(Blog)