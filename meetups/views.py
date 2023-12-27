from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event, Paticipants
from .forms import RegistrationForm


# Create your views here.
def home_page(request):
    events = Event.objects.all()
    return render(request, 'meetups/index.html', {
        'events': events
    })


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

def SignIn(request, ):
    return render(request, 'meetups/sessions/sign_up.html')

def SignUp(request, ):
    return render(request, 'meetups/sessions/sign_up.html')
