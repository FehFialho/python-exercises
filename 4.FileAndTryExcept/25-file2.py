#Aula 6 (20/02/2025)
userWord = input("Escolha uma palavra: ").lower()

with open('Aula 7/file.txt', 'r') as file:
    lyrics = file.read().lower()

words = lyrics.split()  
count = words.count(userWord) 

print(f'A palavra "{userWord}" aparece {count} vezes na música Thunder do Imagine Dragons.')