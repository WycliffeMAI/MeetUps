from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('sign-in', views.SignInPage, name='events-sign-in'),
    path('logout', views.logoutuser, name='logout-user'),
    path('new_user_sign_up', views.SignUp, name='sign-up'),
    path('user/profile', views.userProfile, name='user-profile'),
    path('<slug:event_slug>/success', views.SuccessfulRegistratiion, name='successful-registration'),
    path('<slug:event_slug>', views.event_details, name='event-details'),

]
