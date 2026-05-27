#Aula 3 (17/02/2025)

alfaParaNum = {
    'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 
    'H': '7', 'I': '8', 'J': '9', 'K': '10', 'L': '11', 'M': '12', 'N': '13', 
    'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 
    'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25'
}

numParaAlfa = {
    '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', 
    '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', 
    '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', 
    '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z'
}

mensagem = input('Digite sua mensagem: ').upper()
print(mensagem)

def encriptar(caractere):
    if caractere in alfaParaNum:
        return alfaParaNum[caractere] 
    elif caractere in numParaAlfa:
        return numParaAlfa[caractere]
    return caractere

newMessage = '_'.join(map(encriptar, mensagem))
print(f'Sua senha é: {newMessage}')