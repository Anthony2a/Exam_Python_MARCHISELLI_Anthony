from Tache import *

class GestionTaches():
    def __init__(self) -> None:
        self.list_tache = []


    def ajouter_tache(self, titre, description):
        self.list_tache.append(Tache(titre, description, False))
        return Tache(titre, description, False)
    
    def completer_tache(self, titre):
        if(titre not in self.list_tache):
            print("Task do not exist")
            return "error"
        else:
            titre.setComplete(True)
    
    def verrifier_tache(self, titre):
        if(titre not in self.list_tache):
            print("Task does not exist")
            return "error"
        else : 
            return titre.getComplete()
            
    