from email.mime import image
import django
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Paticipants(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, )
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name}/ {self.email}'


class Locations(models.Model):
    name = models.CharField(max_length=200, )

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200, )
    description = models.TextField()
    organizer_email = models.EmailField(unique=True, )
    date = models.DateField()
    slug = models.SlugField(unique=True, null=False)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Paticipants, )
    image = models.ImageField(upload_to='images', )

    class Meta:
        db_table = 'events names'
        # ordering = ['participants']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("event_details", kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
