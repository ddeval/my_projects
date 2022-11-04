def demander_nbre():
    my_list=[]
    nombre=int(input("Quel nombre ? "))
    for i in range(1,nombre+1):
        my_list.append(i)
    print(my_list)
    my_list.reverse()
    print(my_list)
demander_nbre()
