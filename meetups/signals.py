from platform import java_ver
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Paticipants


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Paticipants.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created == False:
        instance.participants.save()

