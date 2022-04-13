    # Obtener una lista de los números que son pares:

    # Ejemplo 1 con list comprehension
# my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = [i for i in my_list if i % 2 != 0]
# print(odd)

    # Ejemplo 2 utilizando "filter"
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

odd = list(filter(lambda x: x % 2 !=0, my_list))
print(odd)

    # Convertir esta una lista en si misma pero elevada al cuadrado:

    #Ejemplo 1 con list comprehension
# my_own_list = [1, 2, 3, 4, 5]
# squares = [i**2 for i in my_list]
# print(squares)

    #Ejemplo 2 con "map"
my_own_list = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, my_own_list))
print(squares)

    # Reducir los valores de una lista a un unico valor:

    #Ejemplo 1 usando un ciclo for
# my_other_list = [2, 2, 2, 2, 2]
# all_multiplied = 1

# for i in my_other_list:
#     all_multiplied = all_multiplied * i
# print(all_multiplied)

    #Ejemplo 2 usando "reduce"
from functools import reduce
my_other_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a * b, my_other_list)

print(all_multiplied)