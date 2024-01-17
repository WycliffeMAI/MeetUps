import email
from email import message
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Paticipants

# email
import smtplib
subject = 'success'
message = "You have successfully signed up to Let's meet."

text = f'subject:{subject}\n\n{message}'



@receiver(post_save, sender=User)
def create_paticipant(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='paticipants')
        instance.groups.add(group)

        Paticipants.objects.create(user=instance, email=instance.email)

        # email
        email = "odundoklife1@gmail.com"
        receiver_email = 'pythonklife@gmail.com'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, 'cprp utbz lvbk xzxc')
        server.sendmail(email, receiver_email, text)

        print('profile created')
        # cprp utbz lvbk xzxc



# post_save.connect(create_paticipant, sender=User)

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created == False:
        instance.paticipants.save()

        print('paticipant updated')


# post_save.connect(update_user, sender=User)

