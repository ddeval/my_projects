from ex11 import *

chaine_adn = saisie_dune_chaine_adn("Saisir la chaine : ")
# on l'appelle une 2e fois             --> question = "Saisir la séquence : "
sequence = saisie_dune_chaine_adn("Saisir la séquence : ")

print("chaine :", chaine_adn)
print("sequence :", sequence)

# calculs
occurences = occurences_sequence(sequence, chaine_adn)
pourcentage = pourcentage_sequence(sequence, chaine_adn, occurences)

# affichage des résultats
print(f"Il y a {pourcentage}% de \"{sequence}\" dans la chaine \"{chaine_adn}\"")
