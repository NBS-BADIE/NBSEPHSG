# gestion/context_processors.py
from .models import CompteurVisites

def compteur(request):
    """
    Retourne le compteur de visites pour tous les templates.
    Incrémente une seule fois par session.
    """
    if not request.session.get('compteur_incremente', False):
        compteur_obj, created = CompteurVisites.objects.get_or_create(id=1)
        if not created:
            compteur_obj.nombre += 1
        else:
            compteur_obj.nombre = 1
        compteur_obj.save()
        request.session['compteur_incremente'] = True
    else:
        compteur_obj = CompteurVisites.objects.first()
    
    return {
        'compteur_visites': compteur_obj.nombre if compteur_obj else 0
    }

def role_context(request):
    """
    Fournit le rôle de l'utilisateur connecté pour tous les templates.
    """
    if request.user.is_authenticated:
        return {'user_role': getattr(request.user, 'role', None)}
    return {'user_role': None}