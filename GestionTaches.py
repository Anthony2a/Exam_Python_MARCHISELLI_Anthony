from Tache import *

class GestionTaches():
    def __init__(self) -> None:
        self.list_tache = []


    def ajouter_tache(self, titre, description):
        self.list_tache.append(Tache(titre, description))
        return Tache(titre, description)
    
    def completer_tache(self, titre):
        if(titre not in self.list_tache):
            print("Task do not exist")
        else:
            titre.setComplete()
    
    def verrifier_tache(self, titre):
        if(titre not in self.list_tache):
            return titre.getComplete()
        else : 
            print("Task does not exist")
    