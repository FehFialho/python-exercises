loop = 0
number = 0

class Student:
    def __init__(self, name, course, id): 
        self.name = name
        self.course = course
        self.id = id

    def register(self): 
        with open("Python - Prova/students.txt", "a", encoding="utf-8") as file:
            file.write(f'Usuário {self.name}, Curso: {self.course}, ID: {self.id},\n')
        global number 
        number += 1


while loop == 0:

    try:
        name = input('\nInsira o nome do estudante: ')
        course = input('\nInsira o curso: ')
        id = input('\nInsira o número de matrícula: ')
        newStudent = Student(name, course, id)
        newStudent.register() 
        
        loop = int(input('\nDigite 0 para continuar registrando ou outro valor para sair: '))
    except ValueError:
        print('ERRO! Insira os dados novamente!')



print(f'Número de alunos cadastrados: {number}')