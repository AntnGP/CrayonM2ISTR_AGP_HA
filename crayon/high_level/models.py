from django.db import models


# crayon/models.py


class Ville(models.Model):  # Represente une ville
    nom = models.CharField(max_length=200)
    code_postal = models.IntegerField(default=31400)
    prixm2 = models.IntegerField(default=400)

    def __str__(self):
        return f"{self.nom},{self.code_postal}"


class Local(models.Model):  # Represente un batiment situé dans une ville
    nom = models.CharField(max_length=200)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.PROTECT,
    )
    surface = models.IntegerField(default=200)

    def __str__(self):
        return f"local {self.nom} situé a {self.ville.nom},{self.ville.code_postal} d'une sruface de {self.surface}"


class Siege(Local):  # Represente un type de batiment specifique
    def __str__(self):
        return f"Siege social situé à : {self.nom},{self.code_postal}"


class Machine(models.Model):  # Represente une machine situé dans une usine
    nom = models.CharField(max_length=200)
    prix = models.IntegerField(default=1)
    n_serie = models.CharField(max_length=200, default="A")

    def cost(self):
        return self.prix

    def __str__(self):
        return f"Machine {self.nom},{self.n_serie}"


class Usine(Local):  # Represente un type de batiment specifique
    machines = models.ManyToManyField(
        Machine,
        # on_delete=models.PROTECT,  #pas supporté par ManytoMany
    )

    def cost(self):
        cout = 0
        for m in self.machines.all():  # pour toutes les machines (m) de l'uine on recupere le prix par la methode cost et on l'aditionne au prix du terrain
            cout = cout + m.cost()
        for s in self.stock_set.all():  # stock_set est un paramtre generé par l'intepreteur qui liste tous les stocks de l'usine au quel on accede
            cout = cout + s.cost()
        cout = int(self.ville.prixm2) * int(self.surface) + int(cout)
        f"Coute {cout}€"
        return cout

    def __str__(self):
        return f"Usine {self.nom} de {self.ville.nom},{self.ville.code_postal} d'une sruface de {self.surface}m2"


class Objet(models.Model):  # Represente un objet
    nom = models.CharField(max_length=200, default="truc")
    prix = models.IntegerField(default=400)

    def __str__(self):
        return f"{self.nom},{self.prix}"


class Ressource(Objet):  # Represente un type d'objet
    def acheter(self):  # achete une ressource
        prix = {self.prix}
        f"Prix d'achat = {prix}€"
        return prix

    def __str__(self):
        return f"Ressource :{self.nom},{self.prix} "


class Stock(models.Model):  # Represente un type de batiment specifique
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.PROTECT,
    )
    nombre = models.IntegerField(default=0)
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def cost(self):
        cout = self.ressource.prix * self.nombre
        f"Coute {cout}€"
        return cout

    def __str__(self):
        return f"Stock situe a {self.local.nom} dans {self.local.ville.nom},{self.local.ville.code_postal} d'une surface de {self.local.surface}"


class QuantiteRessource(models.Model):  # Represente un enssemble de ressources
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.PROTECT,
    )
    quantite = models.IntegerField(default=0)

    def cost(self):
        cout = self.ressource.prix * self.quantite
        f"Coute {cout}€"
        return cout

    def __str__(self):
        return f"Demande {self.quantite} {self.ressource.nom}"


class Etape(models.Model):  # Represente une etape de production
    nom = models.CharField(max_length=200)
    duree = models.IntegerField(default=0)
    machine = models.ForeignKey(
        Machine,
        on_delete=models.PROTECT,
    )

    ressources = models.ForeignKey(
        QuantiteRessource,
        on_delete=models.PROTECT,
    )
    etape_suivante = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (
            f"Etape demandant {self.ressources.ressource.nom} avec {self.machine.nom}"
        )

    # Une etape ne crée pas de produit car c'est trop compliquer


class Produit(models.Model):  # Represente un objet que l'on vend
    premiere_etape = models.ForeignKey(
        Etape,
        on_delete=models.PROTECT,
    )
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"Demande {self.quantite} {self.ressource.nom}"
