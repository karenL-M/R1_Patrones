from abc import abstractmethod

class Servidor():    
    def mensa(self, mensaje):
        print("/{} servicio: {}".format( mensaje))
      
       
        
    

class ServidorConcreto(Servidor):
     
        self._servidorconcreto = Usuario2(self)
        self._servidorconcreto = Usuario1(self)
       
class Usuario():
    
        self._servidor = Servidor(self)
        
        
        
    
    
    
class Usuario1(Usuario):
    def __init__(self, nombre):
        self.nombre = nombre
        self.servidor = Servido
        def sendAnswer(self, mensaje):
        self.servidor.mensa(self, mensaje)
        

    def __str__(self):
        return self.nombre

class Usuario2(Usuario):
    
    def __init__(self, nombre2):
        self.nombre2 = nombre2
        self.servidor = Servidor
 
    def sendAnswer(self, mensaje):
        self.servidor.mensa(self, mensaje)

    def __str__(self):
        return self.nombre2


ws13 = Usuario('Windows Server 2013')
ws16 = Usuario2('Windows Server 2016')
ubuntuS = Usuario('Ubuntu Server')

 
ws13.sendAnswer("Detenido")
ws16.sendAnswer("Iniciando")
ubuntuS.sendAnswer("Funcionando")

sistema = Usuario('Sistema')
print("\n")
sistema.sendAnswer("Reiniciando servidores.")
sistema.sendAnswer("Reiniciando servidores..")
sistema.sendAnswer("Reiniciando servidores...")
print("\n")
ws13.sendAnswer("Iniciando")
ws16.sendAnswer("Iniciando")
ubuntuS.sendAnswer("Iniciando")
print("\n")
sistema.sendAnswer("Sistemas Funcionando [►]")
