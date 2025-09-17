#Aula 3 (17/02/2025)
num = int(input("Escolha um número para ser somado:"))

fibonacci = [0, 1]

for i in range(num-2):
    proxNumero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proxNumero)

if num < 3:
    print(fibonacci[0:num])
else:
    print(fibonacci)