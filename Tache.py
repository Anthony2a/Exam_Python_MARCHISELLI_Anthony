class Tache():
    def __init__(self, titre, description) -> None:
        self.title = titre
        self.desc = description
        self.completed = False
    
    def __eq__(self, other):
        return self.title == other.title and \
               self.desc == other.desc and \
                self.completed == other.completed

    def setComplete(self):
        self.completed = True

    def getComplete(self):
        return self.completed
