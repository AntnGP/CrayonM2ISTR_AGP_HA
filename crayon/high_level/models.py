from django.db import models


# crayon/models.py

class Ville(models.Model):
    nom = models.CharField(max_length=200)
    code_postal = models.IntegerField(default=31400)
    prixm2 = models.IntegerField(default=400)
    
class Local(models.Model):
    nom = models.CharField(max_length=200)
    ville = models.ForeignKey(
            Ville,
            on_delete=models.PROTECT,
            )
    surface = models.CharField(max_length=200)

class Siege(Local):
    pass # pour dire a python que ce n'est pas une erreur et que l'on ne met rien dedans
   
class Machine(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.IntegerField(default=1)
    n_serie = models.CharField(max_length=200,default='A') 
   
class Usine(Local):
      machine = models.ForeignKey(
            Machine,
            on_delete=models.PROTECT,
            )

