class Address :
    def __init__(self, street, city) :
        self.street = str(street)
        self.city = str(city)

    def show(self) :
        print(self.street)
        print(self.city)

class Person :
    def __init__(self, name, email):
        self.name = name
        self.email= email
    def show(self):
        print(self.name + ' ' + self.email)
        return Address

class Contact(Address, Person) : 
    def __init__(self, name, email, street, city):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self) :
        print(self.name)    
        print(self.email)
        print(self.street)
        print(self.city)

class Notebook  : 
    def __init__(self) :
        self.dico = {}

    def show (self) :
        for name, contact in self.dico.items() : 
            print(f"===={name}====")
            contact.show()

        
    def add(self, name, email, street,city):
        self.dico[name ] = Contact(name, email, street, city)
       
        


        
notes = Notebook()


notes.add('Alice', '<pepette@dog.com>', 'Rde 65', 'Lille')
notes.add('Bob', '<bob@bib.com>', 'Rtb 35', 'Paris')
notes.show()       



          
        