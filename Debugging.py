def divisors(num):
    divisors = [] #lista vacia
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        elif num == 0:
            raise ValueError("\'No puedes ingresar el cero(0) como valor\'")
        for i in range(1,num + 1): #para i en el rango de: 1 al "número hacia si mismo" + 1
            # if num % i == 1: #sí el resto de la division es igual a 1:
            if num % i == 0: # haciendo debugging encontramos el error.
                divisors.append(i) #agregamos numero "i"
        return divisors #retornamos divisors
    except ValueError as ve:
        print(ve)
        return False
    

def main():
    try:
        num = int(input("\nIngresa un número: ")) # solicitamos datos
        print(divisors(num)) # llamamos a la función "divisiors" para los datos solicitados del usuario
    except ValueError:
        print("\nDebes ingresar un número entero positivo")
        main()

if __name__ == '__main__':
    main() # inicio del programa