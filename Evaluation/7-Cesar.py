loop = 0
while loop == 0: 

    try:
        cripto = int(input('Insira uma chave de criptografia de 1 até 25: '))

        if cripto > 25 or cripto <1:
            print('Apenas valores entre 1 e 25!')
            raise ValueError

        word = input('Insira uma palavra para ser criptografada: ').upper()

        alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        wordArray = list(word)
        newWord = []

        for caractere in wordArray:
            try:
                indice = alfa.index(caractere) #Encontrando indice da letra no alfabeto.
                caractere = alfa[indice+cripto] 
                newWord.append(caractere)
            except IndexError:
                caractere = alfa[(indice+cripto)-26]  
                newWord.append(caractere)

        newWord = ''.join(newWord)
        print(f'A nova palavra é {newWord}!')

        loop = int(input('Pressione 0 para continuar, ou qualquer número para sair...'))

    except ValueError:
        print('Erro! Valor incorreto, tente novamente!')