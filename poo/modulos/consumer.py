#from pacote.contas import * # Import global evitar usar
from pacote.contas import somar, subtrair

a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor: '))

print(f'{a} + {b} = {somar(a, b)}')
print(f'{a} - {b} = {subtrair(a, b)}')
