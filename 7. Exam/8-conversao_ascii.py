lista_convertida = []
caracteres = 0

dicio = {
    48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9
}

def divisao():
    print('-' * 30)

def convert(numero):

    divisao() 
    for num in numero:  
        num_ascii = ord(num)
        print(f'Convertendo número: {num_ascii}')
        lista_convertida.append(dicio[num_ascii])
        print(f'O tipo da entrada de {dicio[num_ascii]} é: {type(dicio[num_ascii])}')
        divisao()
        global caracteres   
        caracteres += 1 
    divisao()


# INÍCIO
divisao()
numero = input('Digite um número: ')
print(f'O tipo da entrada é: {type(numero)}') # Aqui não consegui juntar.

convert(numero)
#for i in len(lista_convertida):
#    string += + lista_convertida[i] #Tentei fazer o programa fazer lista_convertida[0] + lista_convertida[1] ... mas não deu certo.