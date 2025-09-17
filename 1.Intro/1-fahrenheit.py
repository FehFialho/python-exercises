#Aula 1 (13/02/2025)

choice = int(input("Digite 1 para converter celsius, 2 para fahrenheit"))

if choice == 1:
    celsius = int(input("Digite a quantidade de graus celsius: "))
    resultado = celsius *1.8 + 32
else:
    fahrenheit = int(input("Digite a quantidade de graus fahrenheit: "))
    resultado = 5 / 9 * (fahrenheit - 32)

print("O resultado é: ", resultado)

nome = "Fernanda"
sobrenome = "Klechowicz"


nomecompleto = nome + sobrenome
print(nomecompleto)

quebra1 = "linha1 \n linha2 \n linha3"

quebra2 = '''linha1
linha 2
linha 3
'''

print(quebra1)
print(quebra2)

s = "p a l a v-r-a"
print(s.split(' '))

print(",".join("ABC"))