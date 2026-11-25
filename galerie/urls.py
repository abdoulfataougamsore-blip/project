from django.urls import path
from . import views
urlpatterns = [
    path('', views.galerie, name='galerie'),
    path('ajouter/', views.ajouter_media, name='ajouter_media'),
    path('modifier/<int:id>/', views.modifier_media, name='modifier_media'),
    path('supprimer/<int:id>/', views.supprimer_media, name='supprimer_media'),
]