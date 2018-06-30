from faker import Faker
fake = Faker()
class Contact:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.next = None

class Libreta:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self,nombre,apellido,telefono,email):
        aux = self.head
        contact = Contact(nombre,apellido,telefono,email)
        if self.count == 0:
            self.head = contact
            self.count += 1
            print (contact.nombre, contact.apellido, "agregado")
        elif self.count == 1:
            if aux.apellido == contact.apellido:
                print("Se intento agregar a",contact.nombre, contact.apellido, "pero este contacto ya existe")
            elif aux.apellido > contact.apellido:
            	self.head.next = aux
            	self.head = contact
            	self.count += 1
            	print(contact.nombre, contact.apellido, "agregado")
            else:
            	self.head = contact
            	contact.next = aux
            	self.count += 1
            	print(contact.nombre, contact.apellido, "agregado")
        else:
        	if aux.apellido > contact.apellido:
        		contact.next = aux
        		self.head = contact
        		self.count += 1
        		print(contact.nombre, contact.apellido, "agregado")
        		return
        	i = 1
        	while(i < self.count):
        		if aux.apellido == contact.apellido:
        			print ("Se intento agregar a",contact.nombre, contact.apellido, "pero este contacto ya existe")
        			return
        		if aux.apellido < contact.apellido and aux.next == None:
        			aux.next = contact
        			self.count += 1 
        			print(contact.nombre, contact.apellido, "agregado")
        			return
        		elif aux.apellido < contact.apellido and aux.next.apellido > contact.apellido:
        			contact.next = aux.next
        			aux.next = contact
        			self.count += 1
        			print(contact.nombre, contact.apellido, "agregado")
        			return
        		else:
        			aux = aux.next

    def delete(self,apellido):
        aux = self.head
        if self.count == 0:
            return print ("No hay contactos que eliminar")
        if self.count == 1:
        	self.head = None
        	self.count = 0
        	print(aux.nombre, "Eliminado")
        i = 1
        while(i < self.count):
        	if aux.apellido == apellido:
        		self.head =aux.next
        		self.count -= 1
        		print(aux.nombre, "Eliminado")
        		return
        	elif aux.next == None:
        		print ("El contacto no existe")
        		return
        	elif aux.next.apellido == apellido:
        		aux.next = aux.next.next
        		self.count -= 1
        		print(aux.nombre, "Eliminado")
        		return
        	else:
        		aux = aux.next


    def print_libreta(self):
        if self.count == 0:
             print("Libreta vacia")
        else:
            temp = self.head
            i = 1
            while temp != None:
                print("Contacto", i,": {} {}, {}, {} ".format(temp.nombre, temp.apellido,temp.telefono,temp.email))
                temp = temp.next
                i += 1	

Libreta = Libreta()
for i in range(1000):
	Libreta.add(fake.first_name(),fake.last_name(),fake.phone_number(),fake.email())
Libreta.print_libreta()
#for i in range(1000):
#	Libreta.delete(fake.last_name())
Libreta.print_libreta()
