#

print('------------------------------------------------------------------------------')

name = str(input('Olá! Qual o seu nome? '))
print('Seja bem-vindo(a), {}!'.format(name))

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Agora, digite a nota do segundo bimestre: '))
n3 = float(input('Já esta quase acabando! Digite a nota do terceiro bimestre: '))
n4 = float(input('Para finalizar, digite a nota do quarto bimestre: '))

m = (n1 + n2 + n3 + n4) / 4

print('---------------------------------------------------------------------------------------------')

print('Prontinho, {}! A média entre as notas {}, {}, {} e {} é igual a: {:.2f}'.format(name, n1, n2, n3, n4, m))

if m < 7:
    print('Reprovado e boas festas!')
else:
    print('Parabéns! Você Passou!')


print('------------------------------------------------------------------------------')