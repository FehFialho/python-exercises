p = input('Digite p: ') # Pede uma palavra. 
n = int(input('Digite n: ')) # Provavelmente uma chave ou regra. 

def funcao(p,n):
    lista = [] # Inicia uma lista vazia.
    for c in p: # Para cada caractere na palavra...
        f = chr((ord(c) - ord('a') + n ) % 26 + ord('a')) 
        # ^ Coloca F como o caractere a partir do { ASCII (Do caractere C no P do usuário) - 97 (Valor do código ASCII de 'a') + N (Segundo atributo do usuário)} % 26 + 97
        lista.append(f) # Adiciona o caractere descriptografado na lista.
    print(''.join(lista))

funcao(p,n)

# Acredito que seja um código de criptografia de alfabeto comum utilizando ASCII, onde o usuário passa uma palavra e algum tipo de chave ou critério.
# Depois que o usuário insere os dois valores, é feito um for que passa por cada caractere do primeiro valor e transforma ele em um outro caractere com base na regra chr((ord(c) - ord('a') + n ) % 26 + ord('a')).