temperature=int(input("Quelle est la température de l'eau? "))
if temperature < 0 :
    print("Solide")
elif temperature >=0 and temperature <=100:
    print("Liquide")
else:
    print("Solide")
