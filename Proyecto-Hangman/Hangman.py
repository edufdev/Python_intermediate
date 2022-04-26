import random
import time
import os
import sys
from time import sleep


def read_words(): # Abrir y leer archivo donde estan los datos
    words= []
    with open('./data/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words


# def normalize(vocal): # Elimina los accentos
#     replacements = (
#         ("á", "a"),
#         ("é", "e"),
#         ("í", "i"),
#         ("ó", "o"),
#         ("ú", "u"),
#     )
#     for a, b in replacements:
#         vocal = vocal.replace(a, b).replace(a.upper(), b.upper())
#     return vocal


def try_again(): #Menú para saber si desea volver a jugar
    nuevo_intento = input('¿Deseas volver a jugar?: Si(s)/Salir(cualquier otra tecla): ')
    if nuevo_intento == 's':
        os.system('clear')
        main()
    else:
        sys.exit()
    


def mecanografiar(texto): # Introducción en modo mecanografico
    for palabras in texto.split():
        sleep(0.2)
        print(palabras, end=' ', flush=True)

print("\n")
os.system('clear')
mecanografiar("Bienvenido  Al  Juego  Del  Ahorcado")
print("\n")
print('''\t  
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
     =====''')
print("\n")
mecanografiar("Adivina la palabra secreta o muere")
print()
mecanografiar("Pierdes una vida cada que te equivocas si te quedas sin vidas pierdes el juego")
print("\n")
time.sleep(2)
os.system('clear')




def main(): # Inicio del programa
    data = read_words()
    chosen_word = random.choice(data)
    word_list = [letter for letter in chosen_word]
    underscore = ["__"] * len(word_list)
    letter_index = {}
    for i, letter in enumerate(chosen_word):
        if not letter_index.get(letter):
            letter_index[letter] = []
        letter_index[letter].append(i)

    fails = 0
    guessed_words = []

    while True:
        print("Adivina la palabra!!!")
        if fails == 1:
            print(f"Tienes {fails} oportunid restante")
        else:
            print(f"Tienes {fails - 1} oportunidades restantes.")
        print(fails)
        print()
        for element in underscore:
            print(element + " ", end="")
        print()


        while True:
            letter = input("Ingresa una letra: ").strip().upper()
            if letter in guessed_words:
                print("Ya intentaste con " + letter + ".\n intenta con otra")
            else:
                if letter.isalpha() == True and len(letter) == 1:
                    guessed_words.append(letter)
                    break
                elif letter.isalpha() == True and len(letter) > 1:
                    print("Solamente puedes ingresar una letra a la vez!")
                else:
                    print("Solo puedes ingresar letras")
    


if __name__ == '__main__':
    main()
    