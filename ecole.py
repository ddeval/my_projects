class Membre:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
      
    def new_member ():
        nom=input("Entrez le nom du nouveau membre")
        prenom=input("Entrez le prénom du nouveau membre")
        nv_member=Membre(nom,prenom)
        return nv_member

    def presentation (self):
        print(f"Bonjour, je m'appelle {self.nom}; {self.prenom}")

    
class Professeur(Membre): 

    def __init__(self, nom, prenom, skill, biographie):
        Membre.__init__(self, nom, prenom)
        if isinstance(skill, list):
            self.skill = skill
        else:
            self.skill = []
        self.biographie=biographie   

class Etudiant(Membre): 

    def __init__(self,motivation):
        self.motivation = motivation      






mbre1=Membre("Dupont","Jean")

mbre1.presentation()
prof=Professeur("Toto", "Tata", 2, 'Je suis professeur')
print(prof.skill)
   

    
    
