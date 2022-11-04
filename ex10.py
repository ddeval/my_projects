pop=int(input("Population actuelle ?\n"))
tx_accr=float(input("Taux d'accroissement en nombre décimal ?\n"))
pop_visee=int(input("Population viséee ?\n"))
annee=1

while pop<pop_visee:
    pop=pop*(1+tx_accr)
    annee+=1
print(annee)