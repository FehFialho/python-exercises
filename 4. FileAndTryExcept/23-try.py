#Aula 6 (20/02/2025)
# try:
# except ValueError:
#raise

class SaldoNegativo(Exception):
    pass

def consultarSaldo(x):
    if x <= 0:
        raise SaldoNegativo
    return x

try:
    x = int(input("num:"))
    consultarSaldo(x)
except SaldoNegativo:
    print('Seu saldo não pode ser negativo!')