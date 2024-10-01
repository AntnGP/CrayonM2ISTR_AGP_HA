from django.db import models


# crayon/models.py

class Ville(models.Model): # Represente une ville
    nom = models.CharField(max_length=200)
    code_postal = models.IntegerField(default=31400)
    prixm2 = models.IntegerField(default=400)
        
    def __str__(self):
        return f"{self.nom},{self.code_postal}"
    
class Local(models.Model): # Represente un batiment situé dans une ville
    nom = models.CharField(max_length=200)
    ville = models.ForeignKey(
            Ville,
            on_delete=models.PROTECT,
            )
    surface = models.CharField(max_length=200)
    
 
    def __str__(self):
        return f"local {self.nom} situé a {self.ville.nom},{self.ville.code_postal} d'une sruface de {self.surface}"

        

class Siege(Local): # Represente un type de batiment specifique
    def __str__(self):
        return f"Siege social situé à : {self.nom},{self.code_postal}"
      
   
class Machine(models.Model): # Represente une machine situé dans une usine
    nom = models.CharField(max_length=200)
    prix = models.IntegerField(default=1)
    n_serie = models.CharField(max_length=200,default='A') 
    
    def __str__(self):
        return f"Machine {self.nom},{self.n_serie}"
        
   
class Usine(Local): # Represente un type de batiment specifique
    machines = models.ManyToManyField(
            Machine,
            #on_delete=models.PROTECT,  #pas supporté par ManytoMany
            )
    def __str__(self):
           return f"Usine {self.nom} de {self.ville.nom},{self.ville.code_postal} d'une sruface de {self.surface}m2"

