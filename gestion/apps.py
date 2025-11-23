from django.apps import AppConfig
from django.db.models import Sum

class GestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion'  # <-- ceci est obligatoire

    def ready(self):
        from django.db.models.signals import post_save, post_delete
        from django.apps import apps

        UniteService = apps.get_model('gestion', 'UniteService')
        ServiceDetail = apps.get_model('gestion', 'ServiceDetail')

        def update_service_lits(sender, instance, **kwargs):
            service = instance.service
            total_lits = service.unites.aggregate(Sum('lits'))['lits__sum'] or 0
            details, _ = ServiceDetail.objects.get_or_create(service=service)
            details.nb_lits = total_lits
            details.save()

        post_save.connect(update_service_lits, sender=UniteService)
        post_delete.connect(update_service_lits, sender=UniteService)
