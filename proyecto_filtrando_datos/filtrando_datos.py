DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

    # Forma de filtrar datos, No. 2

def main():
    pass


    # Forma de filtrar datos, No.1

# def main(): #funcion para filtrar datos
#     all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] #lista que contiene el nombre de los trabajadores en DATA si los trabajadores manejan python

#     all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"] #Lista de los trabajadores en DATA que contiene el nombre de los trabajadores si trabajan en Platzi

#     adults = list(filter(lambda worker: worker["age"] > 18, DATA)) #filtrando datos, de los trabajadores en DATA son mayores de 18 años

#     adults = list(map(lambda worker: worker["name"], adults)) #mapeando los datos de la variable "adults" para obtener su nombre

#     old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA)) #mapeando DATA de los trabajadores que son mayores de 70 años y creando un valor de "Verdadero o Falso" dentro de la DATA

#     for worker in old_people: #Ciclo for de los trabajadores en la variable "old_people"
#         print(worker) #Mostramos en pantalla los nombres de los trabajadores

#     for worker in adults: #Ciclo for de los trabajadores en la variable "adults"
#         print(worker) #Mostramos en pantalla los nombres de los trabajadores

#     for worker in all_platzi_workers: #Ciclo for de los trabajadores en la variable "all_platzi_workers"
#         print(worker) #Mostramos en pantalla los nombres de los trabajadores

#     for worker in all_python_devs: #Ciclo for de los trabajadores en la variable "all_platzi_workers"
#         print(worker) #Mostramos en pantalla los nombres de los trabajadores

if __name__ == '__main__':
    main()
    