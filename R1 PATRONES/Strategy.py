
from types import MethodType
from abc import  abstractmethod

class Ladron():
    
    
    
    def __init__(self, *args, **kwargs):
       
        if kwargs.get('robar', None):
            self.robar = MethodType(kwargs.pop('study'), self)
        self._robar= Estrategia()

    def robar(self):
        
        message = '{} should implement a study method'.format(
            self.__class__.__name__)
        raise NotImplementedError(message)
    

class Estrategia(ABC):
    @abstractmethod
    def _estrategia_robar():
        pass
        
        
        

class Objetivo(Estrategia):
    def _estrategia_robar(self):
        pass
     
       

class EntradaSalida(Estrategia):
    def _estrategia_robar(self):
        pass


class HerramientasEspeciales(Estrategia):
    def _estrategia_robar(self):
        pass
     

       


        
       
    


