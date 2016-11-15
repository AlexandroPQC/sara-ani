from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView

from .models import Event
from .forms import EventForm

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list'

# class CreateEvent(CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/event_form.html'
#     success_url = reverse_lazy('event:events/_list')

def EventView(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('events')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form':form})
