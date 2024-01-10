from django.urls import path
from .views import indexView, contactView, aboutView, connexionView, registerView
from .views import BlogCreate, homeView, listArticles, deleteArticle, updateArticle, deconnexion, listUsers

urlpatterns = [
    path('', indexView, name='index'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name="about"),
    path('connexion/', connexionView, name="connexion"),
    path('register/', registerView, name="register"),
    path('home/', homeView, name="home"),
    path('list-articles', listArticles, name="listArticles"),
    path('Add/', BlogCreate, name="addArticle"),
    path('delete/<int:id>', deleteArticle, name="deleteArticle"),
    path('update/<int:id>', updateArticle, name="updateArticle"),
    path('logout/', deconnexion, name="logout"),
    path('users/', listUsers, name="users"),
]