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

	def _add(self,nombre,apellido,telefono,email,contact):	## Suponiendo que viene de la def add ese contact
		if apellido < contact.apellido:
			if contact.left == None:
				contact.left = Contact(nombre,apellido,telefono,email)
				print(nombre, "ingresado")
				contact.left.padre = contact
				self.actualizarEquilibrio(contact.left)
			else:
				self._add(nombre,apellido,telefono,email,contact.left)
		elif apellido > contact.apellido:
			if contact.right == None:
				contact.right = Contact(nombre,apellido,telefono,email)
				print(nombre, "ingresado")
				contact.right.padre = contact
				self.actualizarEquilibrio(contact.right)
			else:
				self._add(nombre,apellido,telefono,email,contact.right)
		else:
			print("Este contacto ya se encuentra registrado")

	def actualizarEquilibrio(self,contact):
		if contact.equilibrio > 1 or contact.equilibrio < -1:
			self.reequilibrar(contact)
			return
		if contact.padre != None:
			if contact.padre.left == contact:
				contact.padre.equilibrio -=1
			elif contact.padre.right == contact:
				contact.padre.equilibrio +=1
			if contact.padre.equilibrio != 0:
				self.actualizarEquilibrio(contact.padre)
		return

	def rotarIzquerda(self,rotRaiz):
		nuevaRaiz = rotRaiz.right
		if nuevaRaiz.left != None:
			nuevaRaiz.left.padre = rotRaiz
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
		rotRaiz.equilibrio = rotRaiz.equilibrio - 1 - max(nuevaRaiz.equilibrio,0)
		nuevaRaiz.equilibrio = nuevaRaiz.equilibrio - 1 +min(rotRaiz.equilibrio,0)

	def rotarDerecha(self,rotRaiz):
		nuevaRaiz = rotRaiz.left
		rotRaiz.left = nuevaRaiz.right
		if nuevaRaiz.right != None:
			nuevaRaiz.right.padre = rotRaiz
			nuevaRaiz.padre = rotRaiz.padre
		if rotRaiz.padre == None:
			self.root = nuevaRaiz
		else:
			if rotRaiz.padre.right == rotRaiz:
				rotRaiz.padre.right = nuevaRaiz
			else:
				rotRaiz.padre.left = nuevaRaiz
		nuevaRaiz.right = rotRaiz
		rotRaiz.padre = nuevaRaiz
		rotRaiz.equilibrio = rotRaiz.equilibrio + 1 - min(nuevaRaiz.equilibrio,0)
		nuevaRaiz.equilibrio = nuevaRaiz.equilibrio + 1 +max(rotRaiz.equilibrio,0)

	def reequilibrar(self,contact):
		if contact.equilibrio > 0:
			if contact.right.equilibrio == 0:
				self.rotarDerecha(contact.right)
				self.rotarIzquerda(contact)
			else:
				self.rotarIzquerda(contact)
		elif contact.equilibrio < 0:
			if contact.left.equilibrio > 0:
				self.rotarIzquerda(contact.left)
				self.rotarDerecha(contact)
			else:
				self.rotarDerecha(contact)

	def buscar(self,apellido):
		if self.root == None:
			return None
		else:
			return self._buscar(apellido,self.root)

	def _buscar(self,apellido,contact):
		if contact == None:
			return None
		elif apellido == contact.apellido:
			return contact
		elif apellido < contact.apellido and contact.left != None:
			return self._buscar(apellido,contact.left)
		elif apellido > contact.apellido and contact.right != None:
			return self._buscar(apellido,contact.right)

	def delete(self,apellido):
		if self.root == None:
			print ("No hay contactos que eliminar")
			return
		return self.delete_contact(self.buscar(apellido))

	def delete_contact(self,contact):
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

			if contact.padre.left == contact:
				contact.padre.left = child
				self.actualizarEquilibrio(contact.padre)
				print(contact.nombre, "Eliminado")
			else:
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
			self._print(self.root.left)
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
			self._print(self.root.right)
		
	
	def _print(self,contact):
		if contact == None:
			pass
			return
		if contact.left != None:
			print("Contacto: {} {}, {}, {} ".format(contact.left.nombre,contact.left.apellido,contact.left.telefono,contact.email))
		else:
			print("Contacto: {} {}, {}, {} ".format(contact.nombre,contact.apellido,contact.telefono,contact.email))
"""
		if contact == None:
			return
		if contact.left == None or contact.left.left == None:
			if contact.left != None:
				print("Contacto: {} {}, {}, {} ".format(contact.left.nombre, contact.left.apellido,contact.left.telefono,contact.left.email))
				print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
				self._print(contact.left)
			else:
				print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
				self._print(contact.right)
		elif contact.right == None or contact.right.right == None:
			if contact.right != None:
				print("Contacto: {} {}, {}, {} ".format(contact.right.nombre, contact.right.apellido,contact.right.telefono,contact.right.email))
				print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
			else:
				print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))


	def print(self):
		if self.root == None:
			print("La agenda se encuentra vacia")
			return
		return self._print(self.root)

	def _print(self,contact):
		if self.contact.left != None:  # Avanza el nodo más a la izquerda
			self._print(contact.left)

		elif self.contact.left == None and contact.padre.left == contact: # Verifica si es el ultimo nodo a la izquerda
			print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
			self._print(contact.padre.right)

		elif self.contact.padre.right == contact:
			print("Contacto: {} {}, {}, {} ".format(contact.padre.nombre, contact.padre.apellido,contact.padre.telefono,contact.padre.email))
			self._print(contact.padre)

		else:
			print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
			if self.contact.left != None:
				self._print(contact.left)
			elif self.contact.right != None:
				self._print(contact.right)
			else:
				return
"""

Agenda = Agenda()	# lista de contactos vacia
Agenda.print()
#Agenda.add(fake.first_name(),fake.last_name(),"123","123")		#se agrega un contacto
Agenda.add("diego","Caceres","123","123")
Agenda.add("Cesar","Alvarez","123","123")
Agenda.print()
Agenda.add("Gabriela","Acuña","123","123")
Agenda.add("Diaguita","Aguilera","123","123")
Agenda.add("Diegosa","ail","123","123")
Agenda.delete("Acuña")
Agenda.print()