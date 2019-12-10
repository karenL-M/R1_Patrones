from abc import ABC, abstractmethod

class EsterioCars(ABC):
    @abstractmethod
    def action(self):
        pass

class Change_Song(CommandAst):
    def __init__(self, EsterioCars):
        self.esteriocars = EsterioCars()

    def action(self):
        self.esteriocars.Change_Song()
class CommandAst(EsterioCars):
        self._Change_Song = CommandAst()
        self._ Turn_Off = CommandAst()
        self._VolumenUp = CommandAst()
   
    
    
        

class Turn_Off(CommandAst):
    def __init__(self, EsterioCars):
        self.esteriocars = EsterioCars()

    def action(self):
        self.esteriocars.Turn_Off()

class VolumenUp(CommandAst):
    def __init__(self, EsterioCars):
        self.esteriocars = EsterioCars()

    def action(self):
        self.esteriocrs.Volumenup()

class ActionMenu (EsterioCars):
    def Chnage_Song(self):
        print("Cambiar cancion")
        
    def Turn_Off(self):
        print("Apagar")
        
    def Volumenup(self):
        print(" Volumen")

class Invocador():
    
    def __init__(self):
        self._actioner = Change_Song()
        self._actioner= Turn_Off()
        self._actioner= VolumenUp()




        
    
        
        
