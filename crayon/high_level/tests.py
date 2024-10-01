from django.test import TestCase

from .models import Machine


"""class MachineModelTests(TestCase):
   def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(nom="scie", prix=1000, n_serie="1683AI2")
        self.assertEqual(Machine.objects.count(), 2)"""

    class CostTest(Testcase):
        def test_cost(self):
            V1 = Ville.objects.create(nom="scie", code_potal=31670, prixm2 = 2000)
            U1 = V1.usine_set.get(nom="BurgerKing",surface=50)
            M1 = U1.machine_set.get(nom="scie", prix=1000, n_serie="1683AI2")
            M2 = U1.machine_set.get(nom="tasla", prix=2000, n_serie="HPelite720")
            
            R1 = Ressource.object.create
            S1 = Stock.objects.create
            
            