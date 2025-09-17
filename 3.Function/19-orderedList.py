#Aula 4 (18/02/2025)
import random

def createList(min, max, size):

    list = []

    for i in range(size):
        randomNum = random.randint(min, max)
        list.append(randomNum)

    Olist = list.copy()

    for i in range(size):
        for j in range(0, size - i - 1):  
            if Olist[j] > Olist[j+1]:
                Olist[j], Olist[j+1] = Olist[j+1], Olist[j] 

    print(f'Lista: {list}')
    print(f'Lista Ordenada: {Olist}')


createList(1, 10, 5)