from re import template
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event, Paticipants
from .forms import RegistrationForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthorisedUser, allowed_user
from django.contrib.auth.models import Group, User

# Create your views here.
@login_required(login_url='events-sign-in')
@allowed_user(allowed_roles=['admin', ])
def home_page(request):
    events = Event.objects.all()
    return render(request, 'meetups/index.html', {
        'events': events
    })

@login_required(login_url='events-sign-in')
def event_details(request, event_slug):
    selected_event = Event.objects.get(slug=event_slug)
    if request.method == 'GET':
        form = RegistrationForm()

    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            participant_email = form.cleaned_data['email']
            participant_name = form.cleaned_data['name']
            participant, _  = Paticipants.objects.get_or_create(name=participant_name, email=participant_email)
            selected_event.participants.add(participant)
            User = User.objects.get_or_create(name=participant_name, email=participant_email)
            selected_event.participants.add(participant)



            reverse_to = reverse('successful-registration', args= [event_slug])
            return redirect(reverse_to)

    return render(request, 'meetups/event_details.html', {
        'event': selected_event,
        'form': form
    })


def SuccessfulRegistratiion(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    return render(request, 'meetups/success.html', {
        'event': event,
    })

@unauthorisedUser
def SignUp(request, ):

    if request.method == 'GET':
        form = CreateUserForm()
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'You successfully signed up for meetups ' + username)
            Paticipants.objects.create(user=user)
            return redirect('events-sign-in')

        return render(request, 'meetups/sessions/signup.html', {'form':form})

@unauthorisedUser
def SignInPage(request, ):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'username or password is incorrect!')
        user = authenticate(request, username=username, password=password)
    return render(request, 'meetups/sessions/login.html')

def logoutuser(request, ):
    logout(request)
    return redirect('events-sign-in')


def userProfile(request, ):
    return render(request, 'meetups/user.html')


class PasswordResetView:
    template_name = 'registration/password_reset_form.html'