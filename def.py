#Numeros pares até 600:
# Crie um algoritmo que imprima os
# numeros pares de 1 até 600
titulo = "Numeros pares ate 600"
print(f'{titulo:^30}')
for i in range(1, 601, 1): #comeco, final - 1, pulo
    if i % 2 == 0:
        print(i, end=' ')

for i in range(2, 601, 2): #comeco, final - 1, pulo
    print(i, end=' ')

# resp = 's'
# while resp in ('s', 'sim'):
#     x = 0
#     numero = int(input(f'Insira o numero que deseja verificar\n'))
#     for i in range(1, numero+1):
#         if numero % i == 0:
#             x += 1
#     if x == 2:
#         print('Numero Primo :)')
#     else:
#         print('Numero não Primo')
#     resp = input("Deseja consultar outro numero: ").lower()

primo = True
numero = int(input(f'Insira o numero que deseja verificar\n'))
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f'{numero} é primo')
else:
    print(f'{numero} nao é primo')

numero = int(input('Até qual número deseja a soma?\n'))
soma = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        soma += i
        print(soma)

frase = 'Estamos no final do semestre'
for letra in frase:
    print (letra)

palavras = frase.split()
print(palavras)

for palavra in frase.split():
    print(palavra)

estado = input('Insira o estado de onde você é: \n')

if estado == 'sao paulo':
    print('paulista')
elif estado == 'rio de janeiro':
    print('carioca')
elif estado == 'minas gerais':
    print('mineiro')
elif estado == 'bahia':
    print('bahiano')
elif estado == 'ceara':
    print('cearense')
else:
    print('outros esados')


x = 0
while x != 10:
    numero = int(input('Digite o numero que você quer descobrir a terça parte\n'))
    print(numero/3)
    x += 1

print("teste")

# frase = input('Digite a frase para descobrir o Nº de vogais e consoantes\n').lower()
# nvogais = 0
# nconsoantes = 0
# vogais = ['a', 'i', 'u', 'e', 'o']
#
# for i in frase:
#     if i in vogais:
#         nvogais += 1
#     if i != ' ' and i not in vogais:
#         nconsoantes += 1
#
# print(f'A sua frase tem {nvogais} vogais e {nconsoantes} consoantes')


frase = input('Digite a frase para descobrir o Nº de vogais e consoantes\n')
nvogais = 0
nconsoantes = 0


for i in frase:
    if i in 'aeiouAEIOU':
        nvogais += 1
    elif i != ' ':
        nconsoantes += 1 # nconsoantes = nconsoantes + 1

print(f'A sua frase tem {nvogais} vogais e {nconsoantes} consoantes')

# 2 elevado a 4
base = int(input("Entre com o numero base a ser elevado"))
exponenciacao = int(input("Entre com a exponenciacao "))
# base = 2
# exponenciacao = 4
total = 1
count = 1
while count <= exponenciacao:
    total = total * base
    # total = total(1) * 2  = 2 # total = total(2) * 2  = 4
    # total = total(4) * 2  = 8 # total = total(8) * 2  = 16
    count = count + 1
print(f'{base} elevado {exponenciacao} é {total}')

total = 1
for i in range(exponenciacao):
    total = total * base
print(f'{base} elevado {exponenciacao} é {total}')










def calcular_potencia(x,y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    return resultado

x = int(input("Digite o valor de X: "))
y = int(input('Digite o valor de Y:'))

if x > 1 and y >= 2:
    print(f'{x} elevado a {y} = {calcular_potencia(x,y)}')
else:
    print('X deve ser maior que 1 e Y deve ser inteiro maior ou igual a 2.')

# n1 = int(input("Entre com o 1o numero:"))
# n2 = int(input("Entre com o 2o numero:"))
# n3 = int(input("Entre com o 3o numero:"))
#
# if n1>n2:
#     temp = n1
#     n1 = n2
#     n2 = temp
# if n1>n3:
#     temp = n1
#     n1 = n3
#     n3 = temp
# if n2>n3:
#     temp = n2
#     n2 = n3
#     n3 = temp
#
# print(f'Menor:{n1}, Intermediario:{n2}, Maior:{n3}')

n1 = int(input("Entre com o 1o numero:"))
n2 = int(input("Entre com o 2o numero:"))
n3 = int(input("Entre com o 3o numero:"))

if n1>n2:
    n1, n2 = n2, n1
if n1>n3:
    n1, n3 = n3, n1
if n2>n3:
    n2, n3 = n3, n2

print(f'Menor:{n1}, Intermediario:{n2}, Maior:{n3}')

palavra = input('Digite a palavra para descobrir se é palíndromo\n')
reverso = ''

for letra in palavra:
    reverso = letra + reverso
    print(reverso)
# for i in range(len(palavra), -1, -1):
#     reverso = reverso + palavra[i]

if palavra == reverso:
    print(f'{palavra} é palíndromo')
else:
    print(f'{palavra} não é palíndromo')

from time import sleep
min = int(input("Qtos minutos:"))


for m in range(min):
    for s in range(60):
        print(f'{m:02d}:{s:02d}')
        sleep(1)
print(f'{min:02d}:00')
