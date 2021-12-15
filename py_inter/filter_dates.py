from functools import reduce
from typing import List

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

def run ():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    # all_python_devs1 = list(filter(lambda worker : worker["language"] == "python", DATA))
    # all_python_devs1 = list(map(lambda worker: worker["name"], all_python_devs1))


    #all_python_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    #all_python_workers1 = list(filter(lambda worker : worker["organization"] == "Platzi", DATA))
    #all_python_workers1 = list(map(lambda worker: worker["name"], all_python_workers1))


    # all_adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    # all_adults = list(map(lambda worker: worker["name"], all_adults))

    # all_adults1 = [worker["name"] for worker in DATA if worker["age"] > 18]
    
    all_olds = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    all_olds1 = [worker | {"old": worker["age"] > 70} for worker in DATA]

 
 
    for worker in all_olds:
        print(worker)

    for worker in all_olds1:
        print(worker)    


if __name__ == "__main__":
    run()  