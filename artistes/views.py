from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ArtisteForm, PalmaresArtisteForm, PrixArtisteForm
from .models import Artiste, PalmaresArtiste, PrixArtiste


class ArtisteListView(ListView):
    model = Artiste
    template_name = 'artistes/artiste_list.html'
    context_object_name = 'artistes'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        role = self.request.GET.get('role')

        if q:
            queryset = queryset.filter(
                Q(nom__icontains=q)
                | Q(prenom__icontains=q)
                | Q(nationalite__icontains=q)
                | Q(films_realises__titre__icontains=q)
                | Q(films_joues__titre__icontains=q)
            ).distinct()

        if role == 'realisateur':
            queryset = queryset.filter(est_realisateur=True)
        elif role == 'acteur':
            queryset = queryset.filter(est_acteur=True)

        return queryset


class ArtisteDetailView(DetailView):
    model = Artiste
    template_name = 'artistes/artiste_detail.html'
    context_object_name = 'artiste'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['palmares'] = self.object.palmares_artistes.select_related('film')
        return context


class ArtisteCreateView(CreateView):
    model = Artiste
    form_class = ArtisteForm
    template_name = 'artistes/artiste_form.html'
    success_url = reverse_lazy('artistes:liste')


class ArtisteUpdateView(UpdateView):
    model = Artiste
    form_class = ArtisteForm
    template_name = 'artistes/artiste_form.html'
    success_url = reverse_lazy('artistes:liste')


class ArtisteDeleteView(DeleteView):
    model = Artiste
    template_name = 'artistes/artiste_confirm_delete.html'
    success_url = reverse_lazy('artistes:liste')


class PrixArtisteCreateView(CreateView):
    model = PrixArtiste
    form_class = PrixArtisteForm
    template_name = 'artistes/prix_form.html'
    success_url = reverse_lazy('artistes:liste')


class PalmaresArtisteCreateView(CreateView):
    model = PalmaresArtiste
    form_class = PalmaresArtisteForm
    template_name = 'artistes/palmares_form.html'
    success_url = reverse_lazy('artistes:liste')