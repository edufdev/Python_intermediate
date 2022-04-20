def read(): # Función para leer archivos
    numbers = [] # lista vacia
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: # abrimos el archivo "numbers.txt" e indicamos el modo de apertura (r = read), tambien codificamos al español y lo nombramos "f"
        for line in f: # leer cada linea en "f"
            numbers.append(int(line)) # convertimos cada linea en un entero y lo agregamos a la lista
    print(numbers) 
    # imrpimimos


def write(): # Función para escribir en archivos
    names = ["Maria", "Fernanda"] # Lista de nombres
    with open("./archivos/names.txt", "a", encoding="utf-8") as f: # Abrimos el archivo "names.txt", modo
        for name in names: # para cada nombre en nombres hacer:
            f.write(name) # en "f" escribir el nombre
            f.write("\n") # en "f" hacer un salto de linea


def main():
    # read()
    write()


if __name__ == '__main__':
    main()
    