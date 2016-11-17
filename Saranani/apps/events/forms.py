from django import forms
from .models import Event
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
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'webpage' : forms.TextInput(attrs={'class':'form-control'}),
            'attachment' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.CheckboxSelectMultiple(),
            'PlaceSchedule' : forms.CheckboxSelectMultiple(),
        }
