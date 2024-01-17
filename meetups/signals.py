from os import name
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Paticipants


@receiver(post_save, sender=User)
def create_paticipant(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='paticipants')
        instance.groups.add(group)

        Paticipants.objects.create(user=instance, email=instance.email)

        print('profile created')


# post_save.connect(create_paticipant, sender=User)

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created == False:
        instance.paticipants.save()

        print('paticipant updated')


# post_save.connect(update_user, sender=User)

