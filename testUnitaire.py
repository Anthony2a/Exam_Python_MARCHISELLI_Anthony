import unittest
from GestionTaches import *
from Tache import *

class testUnit(unittest.TestCase):    
    def testAjoutTaches(self):
        gest = GestionTaches()
        tacheResult1 = gest.ajouter_tache("Work", "Just Work")
        tacheResult2 = Tache("Work", "Just Work")
        self.assertEqual(tacheResult1, tacheResult2)

    def testVerrifTaches(self):
        gest = GestionTaches()
        tacheResult = Tache("Work", "Just Work")
        self.assertEqual(gest.verrifier_tache(tacheResult), False)

    def testCompleteTaches(self):
        gest = GestionTaches()
        tacheResult = Tache("Work", "Just Work")
        gest.completer_tache(tacheResult)
        self.assertEqual(gest.verrifier_tache(tacheResult), True)

    def testCompleteTachesInexistante(self):
        gest = GestionTaches()


if __name__ == '__main__':
    unittest.main()