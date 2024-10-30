print('Ola Mundo')
nome = 'Pedro'
print('Bem vindo', nome, "!!!", "Este ano sera incrivel")


print('Programa que calcula a media')
#Quando a variavel tem um valor fixo dentro do programa, ela é chamada
#de CONSTANTE
x = 7
y = 9
media = (x + y) / 2
print('Sendo o primeiro numero', x, '\ne o segundo numero', y)
print('A media é', media)


#print('Taximetro')
titulo = "Taximetro"
print(f"{titulo:^30}")

custo_km = 5.5
#km_rodado = 7.8
km_rodado = float(input("Entre com a quantidade de KM rodados: "))
print(type(km_rodado))
#total_pagar = custo_km * float(km_rodado)
total_pagar = custo_km * km_rodado
#titulo + 9
print("O total a pagar é R$", total_pagar)
print("O total a pagar é R${total_pagar:.2f}")
print(f"O total a pagar é R${total_pagar:.9f}")
