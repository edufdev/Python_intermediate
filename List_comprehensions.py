def main(): #Funcion para hacer una lista de 100 numeros enteros elevados al cuadrado
    # squares = [] #inicio de lista    
    # for i in range(1, 101): #para i en rango del 1 hasta el 101
    #     # if i % 3 != 0: # si i su resultado es diferente de 0
    #         squares.append(i**2) # agregar a la lista i elevado al cuadrado
    squares = [i for i in range(36, 100000) if i % 36 == 0]

    print(squares) #imprimir lista

# Indicia el inicio del programa en la funcion main
if __name__ == '__main__': 
    main()