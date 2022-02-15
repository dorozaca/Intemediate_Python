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

def run():

    # Comprehensions solutions
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python'] #FILTRANDO DICCIONARIO CON COMPREHENSION
    for worker in all_python_devs:#Iterando la lista para que nos de los nombre consecutivos y no un array
        print(worker)

    adults=list(filter(lambda i:i['age']>18, DATA)) #FILTRANDO DICCIONARIO CON FILTER - primer paso es filtrar >18 con filter
    adults_name=list(map(lambda i:i['name'], adults))#segundo paso es extraer solo "names" con map
    print(adults_name)

    # old_people=list(map(lambda i:i|{"old":i['age']>70}, DATA)) #usando pipe para sumar dics y crear nuevo dict / No soporta | esta version de python  
    # print(old_people)


if __name__ == '__main__':
    run()