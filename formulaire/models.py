from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

class Donnees(models.Model):
	
    moyenne_au_BAC = models.DecimalField( max_digits=4, decimal_places=2)
    Note_en_francais = models.DecimalField( max_digits=4, decimal_places=2)
    Note_en_philosophie = models.DecimalField( max_digits=4, decimal_places=2)
    Note_en_mathematiques = models.DecimalField(max_digits=4, decimal_places=2)
    Note_en_anglais = models.DecimalField(max_digits=4, decimal_places=2)
    Note_en_geographie = models.DecimalField(max_digits=4, decimal_places=2)
    
    CHOIX_SELECTION = (
        (0, 'A4'),
        (1, 'D'),
        (2, 'C'),
    )
    Serie_du_BAC = models.IntegerField(choices=CHOIX_SELECTION)
    
    CHOIX_SELECTIONFILIERE = (
        (0, 'SEG'),
        (1, 'SID'),
        (2, 'HISTOIRE ET ARCHEOLOGIE'),
        (3, 'GEOGRAPHIE'),
        (4, 'LETTRE MODERNE'),
        (5, 'PHILOSOPHIE'),
               
    )  
    filiere_desiree = models.IntegerField(choices=CHOIX_SELECTIONFILIERE)
       
