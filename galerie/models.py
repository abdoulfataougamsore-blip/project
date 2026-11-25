
from django.db import models
from django.core.exceptions import ValidationError


class Media(models.Model):
    TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Vidéo'),
    ]

    titre = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='galerie/', blank=True)
    lien_video = models.URLField(blank=True)
    legende = models.TextField(blank=True, verbose_name='Légende')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def clean(self):
        if self.type =='image' and not self.fichier:
            raise ValidationError("Une image doit être accompagnée d'un fichier")
        if self.type =='video' and not (self.fichier or self.lien_video ):
            raise ValidationError("Une vidéo doit avoir un fichier ou un lien")