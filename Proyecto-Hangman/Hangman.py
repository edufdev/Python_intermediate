import random
import time
import os
import sys
from time import sleep


def hangman():
    print('    \n¡Excelente, empecemos el juego!\n')

    words = [] 
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f: 
            words.append(line.strip().upper())
    
    la_palabra = random.choice(words).upper()
    palabra_secreta = ['_' for letter in la_palabra]

    vidas = 7
    puntos = 0



def menu():
    
    menu = '''
    menu: 

    1) ¿Desea empezar a jugar?
    2) ¿Desea salir del juego?
    (1) o (2):
    R:// '''

    opciones = int(input(f'\t{menu}'))

    try:
        if opciones == 1:
            return hangman()
        if opciones == 2:
            print('Adios')
            time.sleep(1)
        if opciones > 2:
            print('Ingrese una opcion valida por favor')
            time.sleep(2)
            print('Intente otra vez')
            time.sleep(2)
            main()
        if opciones <= 0:
            print('Ingrese una opcion valida por favor')
            time.sleep(2)
            print('Intente otra vez')
            time.sleep(2)
            main()
    except ValueError:
        print('Ingrese un valor valido')
        print('Intente otra vez')
        time.sleep(2)
        main()


def mecanografiar(texto):
    for palabras in texto.split():
        sleep(0.2)
        print(palabras, end=' ', flush=True)

print("\n")
mecanografiar("Bienvenido  Al  Juego  Del  Ahorcado")
print("\n")
print('''  
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
    =====
    ''')
print("\n")
mecanografiar("Adivina la palabra secreta o muere")
print("\n")
mecanografiar("tienes 7 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes")
print("\n")



def main():
    menu()
    time.sleep(2)

    


if __name__ == '__main__':
    main()
    