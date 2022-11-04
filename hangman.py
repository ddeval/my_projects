from pickle import TRUE
from secrets import randbelow


import random
with open("list_of_words.txt") as f:
    the_list = sorted(word.strip(" ") for line in f for word in line.split())

game_over=False
lives=8
chosen_word=random.choice(the_list)
print(f"Pour tricher le mot à deviner est :{chosen_word}")
word_length=len(chosen_word)

affichage= []
for _ in range (word_length):
    affichage+="_"

while not game_over:
    guess=input("Devinez une lettre ").lower()

    if guess in affichage:
        print(" Lettre déjà demandé ")

    for position in range (word_length):
        letter=chosen_word[position]
        if letter==guess:
            affichage[position]=letter
    
    if guess not in chosen_word:
        print("Mauvaise lettre!!")
        lives=lives-1
        if lives==0:
            game_over=TRUE
            print("Game over!!!")
    
    





