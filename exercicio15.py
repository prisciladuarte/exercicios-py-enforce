print('---------------------------------------')

#Apresentação da feira
print('Olá, somos a feira livre Morada do Abacate')

#Pede o nome do solicitante
nome = input('Por favor, digite o seu nome: ')

print('---------------------------------------')

#Saudações da feira e mostra nome de solicitante
print('Seja bem-vindo(a) {}! Nós da Morada do Abacate, sempre pensamos no seu bem estar,\npor isso oferecemos frutas fresquinhas e orgânicas!'.format(nome))

#Lista para ser mostrada na tela
print(' 0 - Banana\n 1 - Abacaxi\n 2 - Abacate\n 3 - Melancia\n 4 - Manga\n 5 - Laranja\n 6 - Maçã')

#lista para busca interna
lista_de_frutas = ["Banana", "Abacaxi", "Abacate", "Melancia", "Manga", "Laranja", "Maça"]

#Entrada de dados para buscar por número da posição e escolher a fruta
opção = int(input('Qual é o numero da fruta que deseja? '))

#Busca por posição na lista e troca por nome da fruta
if opção == 0:
    print('Você escolheu', lista_de_frutas[0])
elif opção == 1:
    print('Você escolheu', lista_de_frutas[1])
elif opção == 2:
    print('Você escolheu', lista_de_frutas[2])
elif opção == 3:
    print('Você escolheu', lista_de_frutas[3])
elif opção == 4:
    print('Você escolheu', lista_de_frutas[4])
elif opção == 5:
    print('Você escolheu', lista_de_frutas[5])
elif opção == 6:
    print('Você escolheu', lista_de_frutas[6])
else:
    print('Essa opção é inválida')

#Retorno dizendo o nome da pessoa e a fruta que escolheu
print('Boa esccolha, {}! Saude em primeiro lugar! Volte sempre.'.format(nome))

print('---------------------------------------')