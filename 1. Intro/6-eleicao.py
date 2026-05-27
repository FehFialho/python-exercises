#Aula 2 (14/02/2025)

anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = 2025
idade = anoAtual - anoNascimento

print(f"Você tem {idade} anos de idade!")

if idade < 16:
    print("Seu voto não é permitido!")
elif idade > 15 and idade < 18:
    print("Seu voto é facultativo!")
elif idade > 17 and idade < 71:
    print("Seu voto é obrigatório")
else:
    print("Seu voto é facultativo!")