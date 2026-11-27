from django.urls import path
from . import views

app_name = 'artistes'

urlpatterns = [
    path('', views.ArtisteListView.as_view(), name='liste'),
    path('ajouter/', views.ArtisteCreateView.as_view(), name='ajouter'),
    path('<int:pk>/', views.ArtisteDetailView.as_view(), name='detail'),
    path('<int:pk>/modifier/', views.ArtisteUpdateView.as_view(), name='modifier'),
    path('<int:pk>/supprimer/', views.ArtisteDeleteView.as_view(), name='supprimer'),
    path('prix/ajouter/', views.PrixArtisteCreateView.as_view(), name='ajouter_prix'),
    path('palmares/ajouter/', views.PalmaresArtisteCreateView.as_view(), name='ajouter_palmares'),
]