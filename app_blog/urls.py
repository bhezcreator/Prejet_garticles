from django.urls import path
from .views import indexView, contactView, aboutView, connexionView, registerView

urlpatterns = [
    path('', indexView, name='index'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name="about"),
    path('connexion/', connexionView, name="connexion"),
    path('register/', registerView, name="register")
]