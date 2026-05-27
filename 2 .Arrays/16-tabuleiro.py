#Aula 3 (17/02/2025)
numero = int(input("Insira a proporção do tabuleiro:"))
matriz = []

for i in range(numero):
    linha = []
    for j in range(numero):
        linha.append("X")
    matriz.append(linha)

for linha in matriz:
    print(" ".join(linha))