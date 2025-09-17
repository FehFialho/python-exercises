#Aula 4 (18/02/2025)
def operacao(x):

    raiz = x ** 0.5
    quadrado = x * x
    inverso = 1 / x
    fatorial = 1 

    for i in range(x,1,-1):
        fatorial *=i
    
    print(fatorial)
    print(raiz)
    print(quadrado)
    print(inverso)
    

while True:
    escolha = int(input('Digite um valor: '))
    operacao(escolha)
    break