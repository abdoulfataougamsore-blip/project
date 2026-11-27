from django import forms
from .models import Artiste, PrixArtiste, PalmaresArtiste


class ArtisteForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = [
            'nom',
            'prenom',
            'sexe',
            'nationalite',
            'date_naissance',
            'biographie',
            'photo',
            'est_realisateur',
            'est_acteur',
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'biographie': forms.Textarea(attrs={'rows': 4}),
        }


class PrixArtisteForm(forms.ModelForm):
    class Meta:
        model = PrixArtiste
        fields = ['acteur', 'film', 'type_prix', 'edition', 'annee']


class PalmaresArtisteForm(forms.ModelForm):
    class Meta:
        model = PalmaresArtiste
        fields = ['artiste', 'titre_distinction', 'edition', 'annee', 'source', 'film']