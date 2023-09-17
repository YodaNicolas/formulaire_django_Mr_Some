from django.forms import ModelForm
from . import models
from .models import Donnees
from django import forms


class ArbreForm(ModelForm):
	class Meta:
		model = Donnees
		fields = [
            'moyenne_au_BAC', 'Note_en_francais', 'Note_en_philosophie',
            'Note_en_mathematiques', 'Note_en_anglais', 'Note_en_geographie',
            'Serie_du_BAC', 'filiere_desiree'
        ]
            
		widgets = {
            'moyenne_au_BAC':forms.NumberInput(attrs={'class':'form-control ','placeholder':'Moyenne au bac','max':20,'min':0}),
            'Note_en_francais':forms.NumberInput(attrs={'class':'form-control ','placeholder':'Entrez la note','max':20,'min':0}),
            'Note_en_philosophie':forms.NumberInput(attrs={'class':'form-control ','placeholder':'Entrez la note','max':20,'min':0}),
            'Note_en_mathematiques':forms.NumberInput(attrs={'class':'form-control ','placeholder':'Entrez la note','max':20,'min':0}),
            'Note_en_anglais':forms.NumberInput(attrs={'class':'form-control ','placeholder':'Entrez la note','max':20,'min':0}),
            'Note_en_geographie':forms.NumberInput(attrs={'class':'form-control','placeholder':'Entrez la note','max':20,'min':0}),
            'Serie_du_BAC':forms.Select(attrs={'class':'form-select'}),
            'filiere_desiree': forms.RadioSelect(attrs={'class':'',}),
        }

 
