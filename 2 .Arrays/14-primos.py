#Aula 3 (17/02/2025)
num = int(input("Digite um número: "))

if num < 2:
    print(f"{num} não é primo.")
elif num in (2, 3, 5):  
    print(f"{num} é primo.")
elif all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")