#Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quarto números;

print('------------------------------------------------------------------------------')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Agora, digite o segundo número: '))
n3 = float(input('Digite o terceiro número, por favor: '))
n4 = float(input('Só falta você digitar mais um número, para finalizar :) : '))

m = (n1 + n2 + n3 + n4) / 4

print('---------------------------------------------------------------------------------------------')

print('A média entre os números {}, {}, {} e {} é igual a: {:.2f}'.format(n1, n2, n3, n4, m))

print('------------------------------------------------------------------------------')

