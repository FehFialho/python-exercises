a = float(input('Insira o lado A do triângulo: '))
b = float(input('Insira o lado B do triângulo: '))
c = float(input('Insira o lado C do triângulo: '))

if abs((b-c) < a < b + c) and abs((a-c) < b < a + c) and abs((a-b) < c < a + b):
    if a == b == c:
        print('É um triângulo equilátero!')
    elif a == b or b == c or c == a:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Triângulo não existe!')