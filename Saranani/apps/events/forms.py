from django import forms
from .models import Event
from django.forms import formset_factory
from material import *

class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = [
            'title',
            'description',
            'webpage',
            'attachment',
            'category',
            'PlaceSchedule'
        ]
        labels = {
            'title' : 'Título',
            'description' : 'Descripción',
            'webpage' : 'Página Web',
            'attachment' : 'Banner',
            'category' : 'Categoría(s)',
            'PlaceSchedule' : 'Lugar y horario'
        }
        help_texts = {
            'title': ('El título del evento.'),
        }
        widgets = {
            'title' : forms.TextInput(),
            'description' : forms.Textarea(),
            'webpage' : forms.TextInput(),
            'attachment' : forms.TextInput(),
            'category' : forms.CheckboxSelectMultiple(),
            'PlaceSchedule' : forms.CheckboxSelectMultiple(),
        }

        layout = Layout(
            Fieldset("sadjfaskldjf")
        )
