horas = float(input("Quantas horas vc ficou estacionado: "))
total = horas * 5
if total < 35:
    # print("Voce ira pagar", total)
    # print("Voce ira pagar R$", total)
    print(f"Voce ira pagar R${total:.2f}")

else:
    print("Pague R$35.00")

titulo = "Faixa"
print(f"{titulo:^30}")
# fornecer um numero e dizer em que faixa ele se encontra
# se ele estiver de 1 a 10 -> faixa 1
# se ele estiver de 11 a 20 -> faixa 2

# numero = int(input("Forneca um numero: "))
# if numero <1 or numero> 20:
#     print("Faixa invalida")
# else:
#     if numero >= 1 and numero <= 10:
#         print("Faixa 1")
#     elif numero >= 11 and numero <= 20:
#             print("Faixa 2")


numero = int(input("Forneca um numero: "))
#if numero >= 1 and numero <= 10:

if 1 <= numero <= 10:
    print("Faixa 1")
elif numero >= 11 and numero <= 20:
        print("Faixa 2")
else:
    print("Faixa invalida")

#Entre com um numero de 1 a 7 e informe que dia da semana é
#1= domingo e 7 = sabado
titulo = "Dia da semana"
print(f"{titulo:^30}")

#dia = int(input("Forneca um numero de 1 a 7: "))
# if dia == 1:
#     print('Domingo')
#     #dia_extenso = 'Domingo'
# elif dia == 2:
#     print('Segunda')
#     #dia_extenso = 'Segunda'
# elif dia == 3:
#     print('Terca')
#     #dia_extenso = 'Terca'
# elif dia == 4:
#     print('Quarta')
#     #dia_extenso = 'Quarta'
# elif dia == 5:
#     print('Quinta')
#     #dia_extenso = 'Quinta'
# elif dia == 6:
#     print('Sexta')
#     #dia_extenso = 'Sexta'
# elif dia == 7:
#     print('Sabado')
#     #dia_extenso = 'Sabado'
# else:
#     print('Dia invalido')


dia = int(input("Forneca um numero de 1 a 7: "))
if dia == 1:
    dia_extenso = 'Domingo'
elif dia == 2:
    dia_extenso = 'Segunda'
elif dia == 3:
    dia_extenso = 'Terca'
elif dia == 4:
    dia_extenso = 'Quarta'
elif dia == 5:
    dia_extenso = 'Quinta'
elif dia == 6:
    dia_extenso = 'Sexta'
elif dia == 7:
    dia_extenso = 'Sabado'
else:
    dia_extenso = 'Invalido'

print(dia_extenso)
