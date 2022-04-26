import random
import time
import os
import sys
from time import sleep


def read_words(): # Abrir y leer archivo donde estan los datos
    words= []
    with open('./data/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip().lower())
    return words



def try_again(): #Menú para saber si desea volver a jugar
    nuevo_intento = input('¿Deseas volver a jugar?: Si(s)/Salir(cualquier otra tecla): ')
    if nuevo_intento == 's':
        os.system('clear')
        main()
    else:
        sys.exit()


def game():
    data = read_words()
    chosen_word = random.choice(data)

    lives = 7
    guessed_words = []
    undersocer = '_'* len(chosen_word)
    print("Adivina la palabra!!!\n")
    print(f'Tiene {undersocer} espacios')

    while True:

        while True:
            guessed = input("Ingresa una letra: ")
            if guessed !=1 and guessed.isnumeric():
                print("Eso no es una letra intenta con una sola letra")
                time.sleep(2)
                os.system('clear')
            else:
                if guessed.lower() in guessed_words:
                    print("Ya habias intentado con esa letra,\n intenta con otra por favor")
                    time.sleep(2)
                    os.system('clear')
                else:
                    guessed_words.append(guessed)

                    if guessed.lower() in chosen_word:
                        print("Felicidades adivinaste una letra!!!")
                        time.sleep(2)
                        os.system('clear')
                        break
                    else:
                        lives = lives-1
                        print("Te haz equivocado, pierdes una vida")
                        print(f"Tienes {lives} vidas")
                        time.sleep(2)
                        os.system('clear')
                        break

        if lives == 0:
            print("Haz perdido, la computadora gana!")
            print(f"La palabra secreta era {chosen_word}")
            time.sleep(2)
            os.system('clear')
            try_again()
        
        estatus = ""

        missed_words = 0

        for letter in chosen_word:

            if letter in guessed_words:
                estatus = estatus + letter
            else:
                estatus = estatus + "_"
                missed_words = missed_words + 1

        print('Palabra:')
        print(estatus)

        if missed_words == 0:
            print("Felicidades haz ganado")
            print("La palabra secreta es: " + chosen_word)
            time.sleep(2)
            os.system('clear')
            try_again()
    


def mecanografiar(texto): # Introducción en modo mecanografico
    for palabras in texto.split():
        sleep(0.2)
        print(palabras, end=' ', flush=True)

print("\n")
os.system('clear')
mecanografiar("Bienvenido  Al  Juego  Del  Ahorcado")
print("\n")
print(''' 
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
     =====''')
mecanografiar("Instrucciones:")
print("\n")
mecanografiar("- Adivina la palabra secreta")
print()
mecanografiar("- Empiezas el juego con 7 vidas")
print()
mecanografiar("- Pierdes una vida cada que te equivocas, si te quedas sin vidas pierdes el juego")
print()
mecanografiar("- Ten muy en cuenta la ortografía al escribir tus respuestas!!")
print()
time.sleep(4)
os.system('clear')




def main(): # Inicio del programa
    game()
    


if __name__ == '__main__':
    main()
    