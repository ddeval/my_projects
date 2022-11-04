


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email
    def show(self):
        print(self.name + ' ' + self.email)

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
    def show(self):
        print(self.street)
        print(self.city)

class Contact(Address, Person):
    def __init__(self, name, email,street,city):
        Person.__init__(self, name,email)
        Address.__init__(self, street,city)
    def show(self):
        print(self.name)
        print(self.email)
        print(self.street)
        print(self.city)

class Notebook():
    def __init__(self):
        self.dico={}

    def show(dico):
        
        for name, Contact in dico.item():
            print(f"========{name}==========")
            contact.show()

    def add(self,name,email,street,city):
        self.dico[name]=Contact(name,email,street,city)
    


Dupont=Contact("Dupont","pepette@princess.com","Dog street","Lille")
Dupont.show()


