from email import message
from re import M
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Paticipants

# email
import smtplib
from django.core.mail import send_mail
from django.conf import settings


subject = 'success'
message = "You have successfully signed up to Let's meet. Yeeeeeeee"

text = f'subject:{subject}\n\n{message}'



@receiver(post_save, sender=User)
def create_paticipant(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='paticipants')
        instance.groups.add(group)

        paticipant = Paticipants.objects.create(user=instance, email=instance.email)

        # email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [paticipant.email, ],
            fail_silently=False,

        )
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

