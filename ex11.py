# Définition des fonctions :
# On établis leur fonctionnement avant de les utiliser/de les appeller

def verification_adn(chaine):
    # boucle du tableau blanc --> on retourne false si on trouve une erreur
    for lettre in chaine:
        if lettre not in 'actg':
            return False
    return True
    # Exemples d'utilisation :
    # print(verification_adn("abecededeg")) False
    # print(verification_adn("agtctgatgta")) True


def saisie_dune_chaine_adn(question):
    # input de chaine --> mettre en minuscule pour autoriser les saisies du style ACtgAgTTA
    ma_chaine = input(question).lower()

    # verification de chaine avec la fonction verification
    while not verification_adn(ma_chaine):
        print("Erreur de saisie!!!")
        ma_chaine = input(question).lower()

    return ma_chaine


def occurences_sequence(sequence, chaine):
    return chaine.count(sequence)

def pourcentage_sequence(sequence, chaine, occurences):
    return occurences * len(sequence) / len(chaine) * 100

def main():
# Programme principal (pas d'indentation)
# On pourra appeler nos fonctions définies auparavant

# on appelle la fonction une 1ere fois --> question = "Saisir la chaine : "
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

if __name__ == "__main__":
    main()







# def occurences_sequence(sequence, chaine):
#     return chaine.count(sequence)

# def pourcentage_sequence(sequence, chaine, occurences):
#     return occurences * len(sequence) / len(chaine) * 100

# # équivaut à la fonction :
# def proportion_sequence_dans_chaine(sequence, chaine):
#     return chaine.count(sequence) * len(sequence) / len(chaine) * 100