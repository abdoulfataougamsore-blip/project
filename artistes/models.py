from django.db import models

class Artiste(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    nationalite = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    biographie = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artistes/', null=True, blank=True)

    est_realisateur = models.BooleanField(default=False, verbose_name="Réalisateur")
    est_acteur = models.BooleanField(default=False, verbose_name="Acteur")

    class Meta:
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class PrixArtiste(models.Model):
    TYPES_PRIX_ACTEUR = [
        ('PRIX_INTERPRETATION_M', "Prix d'interprétation masculine"),
        ('PRIX_INTERPRETATION_F', "Prix d'interprétation féminine"),
        ('PRIX_HONNEUR_ACTEUR', "Prix honorifique d'interprétation"),
        ('AUTRE', "Autre prix d'acteur"),
    ]

    # Uniquement réservé aux acteurs/actrices
    acteur = models.ForeignKey(
        Artiste,
        on_delete=models.CASCADE,
        related_name='prix_acteur',
        limit_choices_to={'est_acteur': True},
    )
    film = models.ForeignKey(
        'films.Film',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prix_acteurs',
    )
    type_prix = models.CharField(max_length=50, choices=TYPES_PRIX_ACTEUR)
    edition = models.CharField(max_length=50, help_text="Ex: FESPACO 2025")
    annee = models.IntegerField()

    class Meta:
        verbose_name = "Prix d'acteur"
        verbose_name_plural = "Prix des acteurs"
        ordering = ['-annee']

    def clean(self):
        if not self.acteur.est_acteur:
            raise ValidationError("Un prix d'artiste ne peut être attribué qu'à un acteur ou une actrice.")

        if self.type_prix == 'PRIX_INTERPRETATION_M' and self.acteur.sexe != 'M':
            raise ValidationError(
                "Le Prix d'interprétation masculine doit être attribué à un acteur de sexe masculin."
            )

        if self.type_prix == 'PRIX_INTERPRETATION_F' and self.acteur.sexe != 'F':
            raise ValidationError(
                "Le Prix d'interprétation féminine doit être attribué à une actrice de sexe féminin."
            )

    def __str__(self):
        return f"{self.get_type_prix_display()} ({self.annee}) - {self.acteur}"


class PalmaresArtiste(models.Model):
    SOURCE_CHOICES = [
        ('FILM_REALISE', "Prix obtenu par le film du réalisateur (ex: Étalon d'or)"),
        ('PRIX_ACTEUR', "Prix d'interprétation remis à l'acteur/actrice"),
    ]

    artiste = models.ForeignKey(
        Artiste,
        on_delete=models.CASCADE,
        related_name='palmares_artistes',
    )
    titre_distinction = models.CharField(max_length=150)
    edition = models.CharField(max_length=50)
    annee = models.IntegerField()
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)

    film = models.ForeignKey(
        'films.Film',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='entrees_palmares_artistes',
    )
    prix_artiste = models.OneToOneField(
        PrixArtiste,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='entree_palmares',
    )

    class Meta:
        verbose_name = "Palmarès de l'artiste"
        verbose_name_plural = "Palmarès des artistes"
        ordering = ['-annee', 'titre_distinction']

    def __str__(self):
        return f"{self.artiste} — {self.titre_distinction} ({self.annee})"