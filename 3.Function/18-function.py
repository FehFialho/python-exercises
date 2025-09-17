#Aula 4 (18/02/2025)
import time

def count(start,end,x):
    for i in range(start,end,x):
        print(i)
        time.sleep(1)

inicio = int(input('Defina o início do contador: '))
fim = int(input('Defina o fim do contador: '))
passo = int(input('Defina o passo do contador: '))

print(f'==============Contador===============\n | Início - {inicio}| Fim - {fim} | Passo - {passo} |')

count(inicio,fim,passo)