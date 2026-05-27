loop = 1
num_aluno = 0
alunos = []

def novo_aluno(nome,idade,nota_mat,nota_pt,nota_cie):
    print('Cadastrando novo aluno!')
    global num_aluno
    num_aluno += 1
    novo_aluno = ('aluno' + str(num_aluno)) #Criando nome para o dicionário!
    novo_aluno = {}
    novo_aluno['nome'] = nome
    novo_aluno['idade'] = idade
    novo_aluno['nota_mat'] = (nota_mat)
    novo_aluno['nota_pt'] = (nota_pt)
    novo_aluno['nota_cie'] = (nota_cie)
    alunos.append(novo_aluno)

def relatorio():
    for aluno in alunos:
        media = (aluno['nota_mat'] + aluno['nota_pt'] + aluno['nota_cie']) / 3
        print(f'Nome: {aluno['nome']}, Média: {media}')

while loop == 1:
    print('-' * 40)

    nome = input('Insira nome do aluno: ')
    idade = int(input('Insira idade do aluno: '))
    nota_mat = float(input('Insira a nota de Matemática: '))
    nota_pt = float(input('Insira a nota de Português: '))
    nota_cie = float(input('Insira a nota de Ciências: '))
    novo_aluno(nome,idade,nota_mat,nota_pt,nota_cie)

    loop = int(input('Digite 1 para continuar...'))

#print('-' * 40)
#print(f'Array de Alunos: {alunos}')
print('-' * 40)
relatorio()