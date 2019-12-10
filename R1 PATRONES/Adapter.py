from abc import ABC, abstractmethod

class USB(ABC):
    @abstractmethod
    def acceder(self):
        pass

class MicroSD:
   
class USBAdapter(USB):
    def __init__(self):
        self._MicroSD = MicroSD()
    def acceder(self):
       pass

##class Nadar():
##    def __init__(self):
##        self.steven = GuitarraSencilla()
##        self.saul = GuitarraAcustica()
##        self.hector = GuitarraElectricaAdapter()
      


