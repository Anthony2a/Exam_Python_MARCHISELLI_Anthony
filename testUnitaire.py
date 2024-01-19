import unittest
from GestionTaches import *
from Tache import *

class testUnit(unittest.TestCase):    
    def testAjoutTaches(self):
        gest = GestionTaches()
        tacheResult1 = gest.ajouter_tache("Work", "Just Work")
        tacheResult2 = Tache("Work", "Just Work", False)
        self.assertEqual(tacheResult1, tacheResult2)

    def testVerrifTaches(self):
        gest = GestionTaches()
        tacheResult = gest.ajouter_tache("Work", "Just Work")
        self.assertEqual(gest.verrifier_tache(tacheResult), False)

    def testCompleteTaches(self):
        gest = GestionTaches()
        tacheResultACompleter = gest.ajouter_tache("Work", "Just Work")
        gest.completer_tache(tacheResultACompleter)
        self.assertEqual(gest.verrifier_tache(tacheResultACompleter), True)

    def testCompleteTachesInexistante(self):
        gest = GestionTaches()
        self.assertEqual(gest.completer_tache("Don't exist"), "error")

    def testNotInList(self):
        gest = GestionTaches()
        TacheNotInListe = Tache("Hello", "World", False)
        self.assertEqual(gest.verrifier_tache(TacheNotInListe), "error")


if __name__ == '__main__':
    unittest.main()