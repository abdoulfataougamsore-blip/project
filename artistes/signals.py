from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PrixArtiste, PalmaresArtiste


@receiver(post_save, sender=PrixArtiste)
def sync_prix_acteur_vers_palmares(sender, instance, **kwargs):
    PalmaresArtiste.objects.update_or_create(
        prix_artiste=instance,
        defaults={
            'artiste': instance.acteur,
            'titre_distinction': instance.get_type_prix_display(),
            'edition': instance.edition,
            'annee': instance.annee,
            'source': 'PRIX_ACTEUR',
            'film': instance.film,
        },
    )