from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Event
from .forms import EventForm

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list'
    paginate_by = 6

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'

class CreateEvent(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events')


def EventView(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('events')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form':form})

def EditEvent(request, id_event):
    event = Event.objects.get(id=id_event)
    if request.method == 'GET':
        form = EventForm(instance=event)
    else:
        form = EventForm(request.POST, instance=event)
        if form.is_valid:
            form.save()
        return redirect('events')
    return render(request, 'events/event_form.html', {'form':form})

def DeleteEvent(request, id_event):
    event = Event.objects.get(id=id_event)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return render(request, 'events/event_delete.html', {'event':event})


class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events')

class EventDelete(DeleteView):
    model = Event
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('events')
