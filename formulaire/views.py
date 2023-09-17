from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ArbreForm
from .models import Donnees
from . import models
from django import forms 

def index(request):
	submitted = False
	if request.method == "POST":
		form = ArbreForm(request.POST)
		if form.is_valid() :
                            form.save()
                            # RECUPERATION DES DONNEES PROVENANT DU FORMULAIRE
                            bac = form.cleaned_data['moyenne_au_BAC']
                            franc = form.cleaned_data['Note_en_francais']
                            philo = form.cleaned_data['Note_en_philosophie']
                            math = form.cleaned_data['Note_en_mathematiques']
                            anglais = form.cleaned_data['Note_en_anglais']
                            geo = form.cleaned_data['Note_en_geographie']
                            serie = form.cleaned_data['Serie_du_BAC']
                            filiere = form.cleaned_data['filiere_desiree']
                            context = { 'bac': bac,'francais': franc,'philo': philo,
                        'math': math,'anglais': anglais,'geo': geo,
                        'serie': serie,'filiere': filiere, }    
				
		return render(request, 'rendu.html', context)
	else:
		form = ArbreForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, "form.html", {'form': form})


                                                                                            
