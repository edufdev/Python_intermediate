def main():
    # Ejemplo de lo que es una lista y un diccionario
    mi_lista = [1, "Hola", True, 4.5]
    mi_diccionario = {"primer_nombre": "Eduardo", "apellido": "Fuentes"}

    # Se puede agregar diccionarios dentro de listas y listas dentro de diccionarios.

    super_lista = [  # Lista dentro de un diccionario
        {"primer_nombre": "Eduardo", "apellido": "Fuentes"},
        {"primer_nombre": "Juan", "apellido": "Perez"},
        {"primer_nombre": "Pedro", "apellido": "Hernandez"},
        {"primer_nombre": "Tamara", "apellido": "Garcia"},
        {"primer_nombre": "Astrid", "apellido": "Alvarez"},
    ]

    super_diccionario = { # Diccionario dentro de una lista
        "numeros_naturales": [1, 2, 3, 4, 5],
        "numeros_enteros": [-1, -2, 0, 1, 2],
        "numeros_flotantes":[1.1, 4.5, 6.43]
    }
    

    # Para key y value en super diccionario toma lo que contiene
    for key, value in super_diccionario.items():
        # Imprime los valores dentro del diccionario y la lista
        print(key, "=", value)

    # para el item en super lista toma lo que contiene
    for item in super_lista:
        # imprime los nombres y apellidos dentro de la lista y el diccionario
        print(item["primer_nombre"],item["apellido"])

if __name__ == '__main__':
    main()
    