def main(): #Funcion para hacer una lista de 100 numeros enteros elevados al cuadrado
    list = [] #inicio de lista    
    for i in range(1, 101): #para i en rango del 1 hasta el 101
        # if i % 3 != 0: # si i su resultado es diferente de 0
        list.append(i**2) # agregar a la lista i elevado al cuadrado
        print(list) #imprimir lista

# Indicia el inicio del programa en la funcion main
if __name__ == '__main__': 
    main()