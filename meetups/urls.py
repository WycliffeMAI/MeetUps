from . import views
from django.urls import path

urlpatterns = [
    path("meetups/", views.home_page, name='home-page'),
    path('meetups/<slug:event_slug>', views.event_details, name='event-details'),

]
