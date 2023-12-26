from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event
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
            participant = form.save()
            selected_event.participants.add(participant)
            return redirect('home-page')

    return render(request, 'meetups/event_details.html', {
        'event': selected_event,
        'form': form
    })
