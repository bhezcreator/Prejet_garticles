from django.shortcuts import render
from .models import Blog

# Create your views here.

# Affichage de la page accueil du module blog
def indexView(request):

    list_blogs = Blog.objects.all()

    context = {
        'list_blogs' : list_blogs
    }
    return render(request, 'blog/index.html',context)


# Affichage de la page contact du module blog
def contactView(request):
    return render(request, 'blog/contact.html')

# Affichage de la page appropos
def aboutView(request):
    return render(request, 'blog/about.html')
