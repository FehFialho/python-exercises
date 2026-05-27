#Aula 6 (20/02/2025)
userWord = input("Escolha uma palavra: ").lower() 

lyrics = []  
event = 0 

with open('Aula 7/file.txt', 'r') as file:
    for line in file:
        lyrics += line.lower().split()   

for word in lyrics:
    if userWord == word:
        event += 1

print(f'A palavra "{userWord}" aparece {event} vezes na música Thunder do Imagine Dragons.')