from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import MediaForm
from .models import Media

def ajouter_media(request):
    if request.method == 'POST':
        formulaire = MediaForm(request.POST, request.FILES)

        if formulaire.is_valid():
            formulaire.save()
            return redirect('galerie')

    else:
        formulaire = MediaForm()

    return render(request, 'galerie/media_form.html', {
        'formulaire': formulaire
    })

def galerie(request):
    recherche = request.GET.get('q', '')

    medias = Media.objects.all().order_by('-date_ajout')
    if recherche:
        medias = medias.filter(titre__icontains=recherche)
    return render(request, 'galerie/media_list.html', {
        'medias': medias
    })
def modifier_media(request, id):
    media = get_object_or_404(Media, id=id)

    if request.method == 'POST':
        formulaire = MediaForm(
            request.POST,
            request.FILES,
            instance=media
        )

        if formulaire.is_valid():
            formulaire.save()
            return redirect('galerie')

    else:
        formulaire = MediaForm(instance=media)

    return render(request, 'galerie/media_form.html', {
        'formulaire': formulaire,
        'titre_page': 'Modifier un média'
    })
def supprimer_media(request, id):
    media = get_object_or_404(Media, id=id)

    if request.method == 'POST':
        media.delete()
        return redirect('galerie')

    return render(request, 'galerie/media_confirm_delete.html', {
        'media': media
    })