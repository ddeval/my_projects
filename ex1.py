
from ctypes import cast

nom = input("Comment s'appelle le chien ? ")
race = input("Quelle race ? " )
age=input("Quel âge ? ")
# affichage = print("Le chien "+nom+" de race "+race+"a"+age+" ans ")  ne marche pas...
affichage=f"Le chien {nom} de race {race} a {age} ans"
print(affichage)