def mon_decorateur(fonction):
    def wrapper():
        print("Avant décoration:")
        # instructions effectuées avant

        fonction()

        #instruction effectuées après
        print("Après décoration:\nJe décore la fonction")
        fonction()

    return wrapper

@mon_decorateur
def fonction_de_base():
    print("Je suis la fonction de base\n")
    

fonction_de_base()