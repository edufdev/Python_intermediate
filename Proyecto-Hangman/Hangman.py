import random
import time
import os
import sys
from time import sleep

def normalize(vocal): # It removes the accents of a string
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
    for a, b in replacements:
        vocal = vocal.replace(a, b).replace(a.upper(), b.upper())
    return vocal


def hangman():
    print('    \n¡Excelente, empecemos el juego!\n')

    words = [] 
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f: 
            words.append(line.strip().upper())
    
    la_palabra = random.choice(words).upper()
    palabra_secreta = ['_' for letter in la_palabra]
    return palabra_secreta

    vidas = 7
    puntos = 0



def menu():
    nuevo_intento = input('¿Deseas volver a jugar?: (s/n): ')
    if nuevo_intento == 's':
        os.system('clear')
        main()
    else:
        sys.exit()
    


def mecanografiar(texto):
    for palabras in texto.split():
        sleep(0.2)
        print(palabras, end=' ', flush=True)

os.system('clear')
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
mecanografiar("tienes 7 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes")
print("\n")



def main():
    menu = '''
    menu: Seleccione la opción

    1) ¿Empezar a jugar?
    2) ¿Salir del juego?
    R:// '''

    opciones = int(input(f'\t{menu}'))

    try:
        if opciones == 1:
            return hangman()
        if opciones == 2:
            os.system('clear')
            print('Adios')
            time.sleep(1)
            os.system('clear')
        if opciones > 2:
            print('Ingrese una opcion valida por favor')
            time.sleep(2)
            print('Intente otra vez')
            time.sleep(2)
            os.system('clear')
            main()
        if opciones < 1:
            print('Ingrese una opcion valida por favor')
            time.sleep(2)
            print('Intente otra vez')
            time.sleep(2)
            os.system('clear')
            main()
    except ValueError:
        print('Ingrese un valor valido')
        print('Intente otra vez')
        time.sleep(2)
        os.system('clear')
        main()

    


if __name__ == '__main__':
    main()
    