from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('<slug:event_slug>/success', views.SuccessfulRegistratiion, name='successful-registration'),
    path('<slug:event_slug>', views.event_details, name='event-details'),

]
