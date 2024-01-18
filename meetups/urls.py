from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home-page'),

    # login, logout, signup urls
    path('sign-in', views.SignInPage, name='events-sign-in'),
    path('logout', views.logoutuser, name='logout-user'),
    path('new_user_sign_up', views.SignUp, name='sign-up'),


    path('user/profile', views.userProfile, name='user-profile'),
    path('<slug:event_slug>/success', views.SuccessfulRegistratiion, name='successful-registration'),
    path('<slug:event_slug>', views.event_details, name='event-details'),

    # password reset paths
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
