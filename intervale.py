class IntervalError(Exception):
    def __init__(self, message="Erreur: Bornes invalides"):


class Intervalle:
    def __init__(self, valeur_inf:int,valeur_sup:int) -> None:
        self.valeur_inf = valeur_inf
        self.valeur_sup = valeur_sup
        try:
            valeur_inf = int(input("Saisir la valeur inferieure : "))
            valeur_sup = int(input("Saisir la valeur supérieure : "))

            if valeur_sup<valeur_sup  :
                    raise IntervalError()
        except ValueError as ve:
                print(ve)
                print("Saisie invalide !")
                return -1
        except AgeInvalideException as aie: 
                print(aie)
                return -1
        else:
                print("Age valide !")
                return age