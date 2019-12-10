
import copy

class Borrega():
   pass

class Prototype(Borrega):
   tamano = None
   raza = None

   def clonar(self):
      pass
   def obtenerTamano(self):
      return self.tamano
   def obtenerRaza(self):
      return self.raza

class Borrega1(Prototype):
   def __init__(self, numero):
      self.tamano = "Borrega 1"
      self.raza = numero

   def clonar(self):
      return copy.copy(self)

class Borrega2(Prototype):
   def __init__(self, numero):
      self.tamano = "Borrega 2"
      self.raza = numero

   def clonar(self):
      return copy.copy(self)

class Objetos:
   tamano1raza1 = None
   tamano1raza2 = None
   tamano2raza1 = None
   tamano2raza2 = None

   @staticmethod
   def inicializar():
      Objetos.tamano1raza1 = Borrega1(1)
      Objetos.tamano1raza2 = Borrega1(2)
      
      Objetos.tamano2raza1 = Borrega2(1)
      Objetos.tamano2raza2 = Borrega2(2)

   @staticmethod
   def obtenerTamano1Raza1():
      return Objetos.tamano1raza1.clonar()

   @staticmethod
   def obtenerTamano1Raza2():
      return Objetos.tamano1raza2.clonar()

   @staticmethod
   def obtenerTamano2Raza1():
      return Objetos.tamano2raza1.clonar()

   @staticmethod
   def obtenerTamano2Raza2():
      return Objetos.tamano2raza2.clonar()



