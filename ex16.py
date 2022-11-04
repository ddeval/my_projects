from audioop import mul




def operations(nb1,nb2):
    additon=nb1+nb2
    soustraction=nb1-nb2
    multiplication=nb1*nb2
    division=nb1/nb2
    return additon,soustraction,multiplication,division


nb1=float(input("Entrez le premier nombre: \n"))
nb2=float(input("Entrez le deuxième nombre: \n"))
addition,soustraction,multiplication,division=operations(nb1,nb2)
print(f"Le résultat de l'addition est {addition}")
print(f"Le résultat de la soustraction est {soustraction}")
print(f"Le résultat de la multiplication est {multiplication}")
print(f"Le résultat de la division est {division}")