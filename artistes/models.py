from django.db import models

# Create your models here.
class Artiste(models.Model):
    idArtiste = models.AutoField(primary_key=True)
    nomArtiste = models.CharField(max_length=100)
    prenomArtiste = models.CharField(max_length=100)
    paysArtiste = models.CharField(max_length=100)


class Realisateur(Artiste):
    films = models.ManyToManyField("films.Film", related_name="realisateurs")


class Acteur(Artiste):
    films = models.ManyToManyField("films.Film", related_name="acteurs")
