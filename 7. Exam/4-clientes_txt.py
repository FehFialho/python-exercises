dados_tratados = 0

def escrever_cliente(cliente):
    with open ('new_clientes.txt', 'a', encoding='utf-8') as file:
        file.write(cliente)

with open ('clientes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        dados = file.read().lower()

permitidos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

print(dados)
dados_array = dados.split('\n')
print(dados_array)

for i in range(len(dados_array)):
    dado_atual = dados_array[i]
    print(f'Tratando dado: {dado_atual}')
    dados_tratados += 1
    for caracter in dado_atual: # Passa por cada caractere.
        if caracter not in permitidos: # Verifica se está na lista.
            dado_atual = dado_atual.replace(caracter, '') # Remove caracter corrompido.
    escrever_cliente(f'{dado_atual.title()}\n')

print('-' * 40)
print((f'{dados_tratados} dados foram tratados!').center(40))
print('-' * 40)