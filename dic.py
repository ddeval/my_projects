# pour créer un dictionnaire
mon_dict = {} #ne pas confondre avec le set vide (set())

mon_dict = {
    "clé 1": "valeur 1", 
    2: 2, 
    True: False, 
    # ["premier element liste"]: {"valeur1 set"} 
    # une liste avec un set en valeur -> impossible car les clés ne sont que des types simples/primitifs (bool, str, float, int)
}
mon_dict = {
    "test": "valeur pour la clé test",
    1: 340,
    'test': True # la clé étant unique, ici, on remplace la valeur de test
}
print(mon_dict)

# Pour accéder à la valeur liée à la clé d'un dictionnaire,
# on se sert de la syntaxe ci-dessous
print(mon_dict[1])
print(mon_dict['test'])

# Pour ajouter un élément dans un dictionnaire,
# on crée une clé et on lui donne sa valeur
mon_dict['blabla'] = 'Texte lié à blabla'
print(mon_dict)

# Ici , on re-affecte la valeur de 'blabla' à autre chose
mon_dict['blabla'] = 247
print(mon_dict)

# Pour obtenir la liste des clés de notre dictionnaire, il existe la méthode .keys()
print(mon_dict.keys())
for k in mon_dict.keys():
    print(k)

# Pour obtenir les valeurs de notre dictionnaire, il existe la méthode .values()
print(mon_dict.values())
for v in mon_dict.values():
    print(v)


print(mon_dict.items())

# les 3 boucles suivantes font la même chose
for tuple in mon_dict.items():
    cle, valeur = tuple
    print(cle, valeur)