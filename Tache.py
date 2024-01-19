class Tache():
    def __init__(self, titre, description, complete) -> None:
        self.title = titre
        self.desc = description
        self.completed = complete
    
    def __eq__(self, other):
        return self.title == other.title and \
               self.desc == other.desc

    def setComplete(self, boole):
        self.completed = boole

    def getComplete(self):
        return self.completed
