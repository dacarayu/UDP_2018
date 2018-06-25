def str2num(key):
  return sum([ord(c) for c in key])

def hashstr(key,size):
  return str2num(key)%size


class Libreta:
  def __init__(self,size):
    self.list = [None]*size #10
    self.size= size
  
  def agregar(self,nombre,apellido,telefono,email):
    pos = hashstr(apellido,self.size)
    if self.list[pos] is not None:
      print("Se intento agregar a"+apellido+"pero este contacto ya existe")
    else:
      self.list.append([nombre,apellido,telefono,email])
    
  def Imprimir(self,apellido): #20
    pos = hashstr(apellido,self.size)
    for pos in self.list:  
      if pos is apellido:
        print("Contacto: "+ pos[0,1] + " " + e[2]+ " " + e[3])


Libreta = Libreta(3)
Libreta.agregar("Diego","Caceres","1231231","asjkdka")
Libreta.Imprimir("Caceres")
