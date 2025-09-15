from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Movie

@receiver(post_save, sender=Profile)
def assign_movie_permissions(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Movie)
        permissions = Permission.objects.filter(content_type=content_type, codename__in=['add_movie', 'change_movie', 'delete_movie'])
        instance.user.user_permissions.add(*permissions)