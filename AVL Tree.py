import time
from faker import Faker
fake = Faker()
class Contact:
	def __init__(self,nombre,apellido,telefono,email):
		self.nombre = nombre
		self.apellido = apellido
		self.telefono = telefono
		self.email = email
		self.left = None
		self.right = None
		self.padre = None
		self.equilibrio = 0

class Agenda:
	def __init__(self):
		self.root = None

	def add(self,nombre,apellido,telefono,email):
		aux = self.root
		contact = Contact(nombre,apellido,telefono,email)
		if self.root == None:	
			self.root = contact
			print(nombre, "ingresado")
		else:
			self._add(nombre,apellido,telefono,email,self.root)

	def _add(self,nombre,apellido,telefono,email,contact):
		if apellido < contact.apellido:
			#print("Comparando ",contact.apellido + " con "+ apellido)
			if contact.left == None:
				contact.left = Contact(nombre,apellido,telefono,email)
				contact.left.padre = contact
				self.actualizarEquilibrio(contact.left)
				print(nombre,apellido, "ingresado")
				return
			else:
				self._add(nombre,apellido,telefono,email,contact.left)
				return
		elif contact.apellido < apellido:
			#print("Comparando ",contact.apellido + " con "+ apellido)

			if contact.right == None:
				contact.right = Contact(nombre,apellido,telefono,email)
				contact.right.padre = contact
				self.actualizarEquilibrio(contact.right)
				print(nombre,apellido, "ingresado")
			else:
				self._add(nombre,apellido,telefono,email,contact.right)
		elif apellido == contact.apellido:
			print("Este contacto ya se encuentra registrado")

	def actualizarEquilibrio(self,contact):
		if contact.equilibrio > 1 or contact.equilibrio < -1:
			self.reequilibrar(contact)
			return
		if contact.padre != None:
			if contact.padre.left == contact:
				contact.padre.equilibrio +=1
			elif contact.padre.right == contact:
				contact.padre.equilibrio -=1
			if contact.padre.equilibrio != 0:
				self.actualizarEquilibrio(contact.padre)

	def rotarIzquerda(self,rotRaiz):
		#print(rotRaiz.apellido, "Rotado a la izquerda")
		nuevaRaiz = rotRaiz.right
		rotRaiz.right = None
		if nuevaRaiz.left != None:
			nuevaRaiz.left.padre = rotRaiz
			rotRaiz.right = nuevaRaiz.left
		nuevaRaiz.padre = rotRaiz.padre
		if rotRaiz.padre == None:
			self.root = nuevaRaiz
		else:
			if rotRaiz.padre.left == rotRaiz: 
				rotRaiz.padre.left = nuevaRaiz
			else:
				rotRaiz.padre.right = nuevaRaiz

		nuevaRaiz.left = rotRaiz
		rotRaiz.padre = nuevaRaiz
		rotRaiz.equilibrio = rotRaiz.equilibrio + 1 + max(nuevaRaiz.equilibrio,0)
		nuevaRaiz.equilibrio = nuevaRaiz.equilibrio - 1 + max(rotRaiz.equilibrio,0)

	def rotarDerecha(self,rotRaiz):
		#print(rotRaiz.apellido, "Rotado a la derecha")
		nuevaRaiz = rotRaiz.left
		rotRaiz.left = None
		if nuevaRaiz != None and nuevaRaiz.right != None:
			nuevaRaiz.right.padre = rotRaiz
			rotRaiz.left = nuevaRaiz.right
		if nuevaRaiz != None:
			nuevaRaiz.padre = rotRaiz.padre
		else:
			return
		if rotRaiz.padre == None:
			self.root = nuevaRaiz
		else:
			if rotRaiz.padre.right == rotRaiz:
				rotRaiz.padre.right = nuevaRaiz
			else:
				rotRaiz.padre.left = nuevaRaiz

		nuevaRaiz.right = rotRaiz
		rotRaiz.padre = nuevaRaiz
		rotRaiz.equilibrio = rotRaiz.equilibrio - 1 - min(nuevaRaiz.equilibrio,0)
		nuevaRaiz.equilibrio = nuevaRaiz.equilibrio + 1 +max(rotRaiz.equilibrio,0)

	def reequilibrar(self,contact):
		if contact.equilibrio < 0:
			if contact.right != None and contact.right.equilibrio > 0:
				self.rotarDerecha(contact.right)
				self.rotarIzquerda(contact)
			else:
				self.rotarIzquerda(contact)
		elif contact.equilibrio > 0:
			if contact.left != None and contact.left.equilibrio < 0:
				self.rotarIzquerda(contact.left)
				self.rotarDerecha(contact)
			else:
				self.rotarDerecha(contact)

	def buscar(self,apellido):
		if self.root == None:
			return None
		else:
			contact = self._buscar(apellido,self.root)
			return contact

	def _buscar(self,apellido,contact):
		print("No se encontro el contacto")
		if contact == None:
			pass 
		if apellido == contact.apellido:
			return contact
		elif apellido < contact.apellido and contact.left != None:
			self._buscar(apellido,contact.left)
			return contact
		elif apellido > contact.apellido and contact.right != None:
			self._buscar(apellido,contact.right)
			return contact
		#else:

	def delete(self,apellido):
		if self.root == None:
			print ("No hay contactos que eliminar")
			return
		contact = self.buscar(apellido)
		print (contact.nombre)
		return self.delete_contact(contact)

	def delete_contact(self,contact):
		print(contact)
		def number_children(contact):
			number_children = 0
			if contact.left != None:
				number_children +=1
			if contact.right != None:
				number_children +=1
			return number_children

		if number_children(contact) == 0:
			if contact.padre.left == contact:
				contact.padre.left = None
				self.actualizarEquilibrio(contact.padre)
				print(contact.nombre, "Eliminado")
			else:
				contact.padre.right = None
				self.actualizarEquilibrio(contact.padre)
				print(contact.nombre, "Eliminado")

		if number_children(contact) == 1:
			if contact.left != None:
				child = contact.left
			else:
				child = contact.right

			if contact.padre != None and contact.padre.left == contact:
				contact.padre.left = child
				self.actualizarEquilibrio(contact.padre)
				print(contact.nombre, "Eliminado")
			else:
				if contact.padre != None:
					contact.padre.right = child
					self.actualizarEquilibrio(contact.padre)
					print(contact.nombre, "Eliminado")
			child.padre = contact.padre

		if number_children(contact) == 2:
			successor = contact.right
			contact = successor
			self.actualizarEquilibrio(contact.padre)
			print(contact.nombre, "Eliminado")
			self.delete_contact(successor)

	def print(self):
		if self.root == None:
			print("La agenda se encuentra vacia")
			return
		elif self.root != None:
			contact = self.root
			self._print(contact.left)
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
			self._print(contact.right)
		
	
	def _print(self,contact):
		if contact == None:
			return

		if contact.left != None:
			if contact.right != None:
				self._print(contact.left)
				print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
				self._print(contact.right)
				return	
			else:
				self._print(contact.left)
				print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
			return

		elif contact.right == None and contact.left != None:
			self._print(contact.left)
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))

		elif contact.right != None and contact.left == None:
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
			self._print(contact.right)

		elif contact.right == None and contact.left == None:
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
		else:
			return

Agenda = Agenda()	# lista de contactos vacia
for i in range(1000):
	Agenda.add(fake.first_name(),i,fake.phone_number(),fake.email())
	time_add = time.process_time()
Agenda.print()
print("en agregar contactos tardo: ", time_add, "segundos")
Agenda.print()