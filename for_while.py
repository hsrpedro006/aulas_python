calculo = 6 / 4
print(f"divisao {calculo}")
calculo = 6 // 4
print(f"divisao inteira {calculo}")
calculo = 6 % 4
print(f"resto {calculo}")

print("Tabuada com For")

# num = 5
# tabuada = 1 * num
# print(num, "X", "1", "=", tabuada)
#
# tabuada = 2 * num
# print(num, "X", "2", "=", tabuada)

num = int(input("Entre com o numero da tabuada: "))
for i in range(1, 11):
    tabuada = i * num
    print(f"{num} X {i} = {tabuada}")



titulo = "Tabuada While"
print(f"{titulo:^30}")

num = int(input("Entre com o numero da tabuada: "))
i = 1
while i <= 10:
    tabuada = i * num
    print(f"{num} X {i} = {tabuada}")
#    print(f"{num} X {i} = {i * num}")
    i += 1


titulo = "Divisiveis por 5"
print(f"{titulo:^30}")

num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))

if num1 > num2:
    # temp = num1
    # num1 = num2
    # num2 = temp

    num1, num2 = num2, num1

print(f"numeros divisiveis por 5 entre {num1} e {num2}:")
for i in range(num1, num2 + 1):
    if i % 5 == 0:
        print(i, end=' ')

import time
titulo = "Contagem regressiva"
print(f"{titulo:^30}")

for cont in range(60,-1,-1):
    time.sleep(1)
    print(cont)

titulo = "Fibo"
print(f"{titulo:^30}")

# termo = 8
# prim = 0
# seg = 1
# print(prim)
# print(seg)
# i = 2
# while i < termo:
#     soma = prim + seg
#     print(soma)
#     prim = seg
#     seg = soma
#     i += 1

termo = int(input("Entre com o nro de termos do Fibonacci: "))
prim = 0
seg = 1
if termo == 1:
    print(prim, end = ' ')
elif termo >= 2:
    print(prim, end = ' ')
    print(seg, end = ' ')
    i = 2
    while i < termo:
        soma = prim + seg
        print(soma, end = ' ')
        prim, seg = seg, soma
        i += 1
else:
    print("Numero de termos invalido")