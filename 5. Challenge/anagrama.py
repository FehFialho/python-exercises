import random
loop = 1
score = 100
win = 0
loose = 0

while loop == 1:
    try:

        def encrypt(word): #Cria uma cópia do array word, encriptografa e retorna o array misturado.

            clone = []
            final = []

            for caractere in word:
                clone.append(caractere)
            length = len(clone)
            indices = []

            while len(indices) < length:
                randIndi = random.randint(0, length-1)
                if randIndi not in indices:
                    final.append(clone[randIndi])
                    indices.append(randIndi)

            return final

        def menu():
            print(f'======JOGO DOS ANAGRAMAS======\nScore: {score}\nVitórias: {win}\nDerrotas: {loose}\n==============================')

        def getRandom(): #Pega uma palavra aleatória de acordo com a escolha do usuário.
            if diff == 1:
                randomWord= random.randint(0, 3)
                print('Você escolheu a dificuldade fácil!')
            elif diff == 2:
                randomWord= random.randint(4, 8)
                print('Você escolheu a dificuldade média!')
            elif diff == 3:
                randomWord= random.randint(9, 11)
                print('Você escolheu a dificuldade difícil!')
            else:
                print('Faça uma escolha válida!')
            return randomWord

        with open ('Tigresas/banco.txt', 'r') as file:
            text = file.read()

        listOfWords = text.split() 
        menu()

        bet = int(input('Quantos pontos você deseja apostar?:'))
        while bet > score:
            print('Erro! Você não pode apostar mais pontos do que tem!\n------------------------------------------')
            bet = int(input('Quantos pontos você deseja apostar?'))

        diff = int(input('Qual dificudade você deseja?'))

        word = listOfWords[getRandom()]
        print('#',word)

        while True:

            print(f'Palavra escolhida: {''.join(encrypt(word))}')
            guess = input("Chute:").upper()

            if word == guess:
                score += bet
                win += 1
                print(f'------------------------------------------\nParabéns! Você acertou! A resposta é {word}!\nSeu novo score é {score} pontos!\n------------------------------------------')
                break
            else:
                print(f'------------------------------------------\nErrado! Você perdeu {bet} pontos!\n------------------------------------------')  
                score -= bet
                loose += 1
                if score < 1:
                    print('===========GAME OVER=========\nInfelizmente seus pontos acabaram...\n=========================')
                    loop = 0
                    menu()
    except ValueError:
        print('INSIRA VALOR VÁLIDO!')