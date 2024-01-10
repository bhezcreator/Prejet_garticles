from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .form import BlogForms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from .form import UserForm

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

# Affichage de la page connexion
def connexionView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
    return render(request, 'blog/connexion.html')

# Affichage de la page création de compte User
def registerView(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès!")
            return redirect('connexion')
        else:
            messages.error(request, form.errors)

    return render(request, 'blog/register.html', {'form':form})

"""_Deconnexion_
    Cette fonction aide à se déconnecter de l'application
Returns:
    _type_: _A la page de connexion_
"""
@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

    # Affichage de la page home de l'admin
def homeView(request):
    return render(request, 'admin/home.html')

    """Fonction de traitement des articles du
        coté de l'admin
    """

@login_required
def listUsers(request):
    users = User.objects.all()
    context = {
      'users' : users
    }
    return render(request, 'admin/users.html', context)


@login_required
def listArticles(request):
    list_blogs = Blog.objects.all()
    context = {
        'list_blogs' : list_blogs
    }
    return render(request, 'admin/list_articles.html', context)

# Création des formulaire d'ajout de l'article
@login_required
def BlogCreate(request):
    form = BlogForms(request.POST, request.FILES or None)
    # Vérification de validation des données
    if form.is_valid():
        # Sauvegarder les données
        form.save()
        return redirect('listArticles')
    return render(request, 'admin/add_article.html', {'form':form})

@login_required
def deleteArticle(request, id):
    # article = Blog.objects.get(id=id)
    article = get_object_or_404(Blog, id=id)
    # if request.method == "POST":
    article.delete()
    return redirect('listArticles')

@login_required
def updateArticle(request, id):
    article = get_object_or_404(Blog, id=id)
    form = BlogForms(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('listArticles')

    return render(request, 'admin/update_article.html', {"form":form})