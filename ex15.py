import statistics


note=int(input("Veuillez enrter une note entre 0 et 20 compris. une saisie négative stoppera la saisie\n"))
liste_notes=[]
while note>0:
    note=int(input("Veuillez enrter une note entre 0 et 20 compris. une saisie négative stoppera la saisie\n"))
    if note >0 or note<20:
        liste_notes.append(note)
    else:
        print("Saisie incorrecte!!!")
        # note=int(input("Veuillez enrter une note entre 0 et 20 compris. une saisie négative stoppera la saisie\n"))
            
note_max=max(liste_notes)
note_min=min(liste_notes)
moyenne=round(statistics.mean(liste_notes),2)

print(f"La note maximale est de {note_max}")
print(f"La note minimale est de {note_min}")
print(f"La moyenne est de {moyenne}")