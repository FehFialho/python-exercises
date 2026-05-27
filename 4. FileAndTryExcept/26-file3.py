#Aula 6 (20/02/2025)
unicos = []
itensRepetidos = []

with open ('Aula 7/file.txt', 'w') as file:
    text = file.read()

with open ('Aula 7/listaAtualizada.txt', 'w') as file:
    text = file.read()

listaDeCompras = text.split() 

for item in listaDeCompras:
    if item in unicos:
        itensRepetidos.append(item)
    else:
        unicos.append(item)

print(f'Sua lista de compras possuí {len(unicos)} itens!')
print(f'Os seguintes itens estão repetidos: {itensRepetidos}')