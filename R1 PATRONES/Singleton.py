class ComidaOrfanato(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ("Macarrones con queso, huevo, caldo pollo. Identificador")+str(id(cls))
        return cls.instance

Lunes = ComidaOrfanato()
Martes = ComidaOrfanato()
Miercoles = ComidaOrfanato()
Jueves = ComidaOrfanato()
Viernes = ComidaOrfanato()
Sabado = ComidaOrfanato()
Domingo = ComidaOrfanato()

print("El menú dado a los niños sera \n"+
      "Lunes: "+ Lunes+
      "\nMartes: "+ Martes +
      "\nMiercoles: "+Miercoles+
      "\nJueves: "+Jueves+
      "\nViernes: "+Viernes+
      "\nSabado: "+ Sabado +
      "\nDomingo: "+ Domingo)
