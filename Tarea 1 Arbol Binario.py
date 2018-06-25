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
        self.parent = None

class Libreta:
    def __init__(self):
        self.root = None

    def add(self,nombre,apellido,telefono,email):
        aux = self.root
        contact = Contact(nombre,apellido,telefono,email)
        if self.root == None:   #Estar vacio
            self.root = contact
        else:
            self._insert(nombre,apellido,telefono,email,self.root)

    def _insert(self,nombre,apellido,telefono,email,contact):
        if apellido < contact.apellido:
            if contact.left == None:
                contact.left = Contact(nombre,apellido,telefono,email)
                print(contact.nombre, "agregado")
                contact.left.parent = contact
            else:
                self._insert(nombre,apellido,telefono,email, contact.left)
        elif apellido > contact.apellido:
            if contact.right == None:
                contact.right = Contact(nombre,apellido,telefono,email)
                print(contact.nombre, "agregado")
                contact.right.parent = contact
            else:
                self._insert(nombre,apellido,telefono,email, contact.right)
        else:
            print("Este contacto ya ese encuentra registrado")

    def buscar(self,apellido):
        if self.root==None:
            return None
        else:
            return self._find(apellido, self.root)

    def _find(self, apellido, contact):
        if contact == None:
            return None
        elif apellido == contact.apellido:
            return contact
        elif apellido < contact.apellido and contact.left != None:
            return self._find(apellido, contact.left)
        elif apellido > contact.apellido and contact.right != None:
            return self._find(apellido, contact.right)


    def delete(self, apellido): #Implementar
        if self.root==None:
            return None
        return self.delete_node(self.buscar(apellido))

    def delete_node(self, contact):
        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = contact.parent # Get the parent of the node to be deleted
        node_children = number_children(contact)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == contact:
                node_parent.left = None
                print(contact.nombre, "Eliminado")
            else:
                node_parent.right = None
                print(contact.nombre, "Eliminado")
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if contact.left != None:
                child = contact.left
            else:
                child = contact.right

            # Replace the node to be deleted with its child
            if node_parent.left == contact:
                node_parent.left = child
                print(contact.nombre, "Eliminado")
            else:
                node_parent.right = child
                print(contact.nombre, "Eliminado")

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = contact.right # Get the inorder successor of the deleted node
            contact = successor # Copy the value
            print(contact.nombre, "Eliminado")
            self.delete_node(successor)


    def in_order(self): #Implementar
        if self.root==None:
            print("La agenda se encuentra vacia")
        return self._in_order(self.root)

    def _in_order(self,contact):
        if contact.left != None:
            print("Contacto: {} {}, {}, {} ".format(contact.nombre, contact.apellido,contact.telefono,contact.email))
        else:
            self._in_order(contact.right)



Libreta = Libreta()  # lista de contactos vacia
Libreta.add("Alvaro","Zapata","123","123")    #se agrega un contacto
Libreta.add("diego","Caceres","123","123")
Libreta.add("Cesar","Alvarez","123","123")
Libreta.add("Cesar","Acuña","123","123")
Libreta.delete("Acuña")
print(Libreta.in_order())