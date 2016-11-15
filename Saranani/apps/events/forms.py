from django import forms
from .models import Event
from material import *
class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = [
            'title',
            'description',
            'state',
            'webpage',
            'attachment',
            'PlaceSchedule'
        ]
        labels = {
            'title' : 'Título',
            'description' : 'Descripción',
            'state' : 'Estado',
            'webpage' : 'Página Web',
            'attachment' : 'Banner',
            'PlaceSchedule' : 'Lugar y horario'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'webpage' : forms.TextInput(attrs={'class':'form-control'}),
            'attachment' : forms.TextInput(attrs={'class':'form-control'}),
            'PlaceSchedule' : forms.CheckboxSelectMultiple(),
        }
