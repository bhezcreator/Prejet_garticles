from django.shortcuts import render

# Create your views here.

# Affichage de la page accueil du module blog
def indexView(request):
    return render(request, 'blog/index.html')


# Affichage de la page contact du module blog
def contactView(request):
    return render(request, 'blog/contact.html')

# Affichage de la page appropos
def aboutView(request):
    return render(request, 'blog/about.html')
