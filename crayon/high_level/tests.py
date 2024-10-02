from django.test import TestCase
from .models import Ville, Stock, Ressource, Usine, Machine

"""class MachineModelTests(TestCase):
def test_machine_creation(self):
     self.assertEqual(Machine.objects.count(), 0)
     Machine.objects.create(nom="scie", prix=1000, n_serie="1683AI2")
     self.assertEqual(Machine.objects.count(), 2)"""


class CostTest(TestCase):
    def test_cost(self):
        V1 = Ville.objects.create(nom="Oran", code_postal=31670, prixm2=2000)

        U1 = Usine.objects.create(nom="BurgerKing", ville=V1, surface=50)

        M1 = Machine.objects.create(nom="scie", prix=1000, n_serie="1683AI2")
        U1.machines.add(
            M1
        )  # pour du many to many , il faut faire un objet_set puis l'ajouter avec add()
        M2 = Machine.objects.create(nom="tasla", prix=2000, n_serie="HPelite720")
        U1.machines.add(M2)

        R1 = Ressource.objects.create(nom="Bois 1kg", prix=10)  # 1000
        R2 = Ressource.objects.create(nom="Graphite 1m", prix=15)  # 50
        Stock.objects.create(ressource=R1, nombre=1000, local=U1)
        Stock.objects.create(ressource=R2, nombre=50, local=U1)

        self.assertEqual(Usine.objects.first().cost(), 110750)
        f"Valeur = {U1.cost()}"
