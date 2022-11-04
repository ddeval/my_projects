class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return (self.longueur+self.largeur)*2

    def aire(self):
        return self.longueur*self.largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur,largeur)
        self.hauteur=hauteur
    def perimetre(self):
        return self.longueur+self.largeur*2

    def aire(self):
        return 2*(self.longueur*self.largeur+self.longueur*self.hauteur+self.largeur*self.hauteur)
        
    def volume(self):
        return super().aire()*self.hauteur


if __name__ == "__main__":
    form=Rectangle(4,5) 
    form2=Parallelepipede(4,5,8) 
    print(form.aire())
    print(form.perimetre())
    print(form2.volume())
    print(form2.aire())