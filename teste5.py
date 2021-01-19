
print('-------------------------------------------------------------')

#Saudação inicial
print('Seja bem-vindo(a) a biblioteca Capitu')

#Perguntar nome
nome = input('Qual seu nome? ')

#Printar nome e dizer que vai mostrar os livros
print('Certo, {}! Agora escolha o livro que deseja emprestar:'.format(nome))

#Mostrar opção de livros
lista_de_livros = ["Dom Casmurro - Machado de Assis", "Dom Quixote - Miguel de Cervantes", 
"Cem Anos de Solidão - Gabriel Garcia Marquez", "Revolução dos bichos -  George Orweel",
 "Hamlet - William Shakspeare", "Orgulho e Preconceito - Jane Austen", "O pequeno Principe - Antoine de Saint-Exupéry"]

#Entrada de dados para buscar por número da posição e escolher o livro
opção = int(input('Qual é a sua opção? '))

#Busca por posição na lista e troca por titulo do livro
if opção == 0:
    print(lista_de_livros[0])
elif opção == 1:
    print(lista_de_livros[1])
elif opção == 2:
    print(lista_de_livros[2])
elif opção == 3:
    print(lista_de_livros[3])
elif opção == 4:
    print(lista_de_livros[4])
elif opção == 5:
    print(lista_de_livros[5])
elif opção == 6:
    print(lista_de_livros[6])
elif opção == 7:
    print(lista_de_livros[7])
else:
    print('Essa opção é inválida')

#Retorno dizendo o nome da pessoa e o livro que escolhe
print('Parabéns, {}! você escolheu o livro {}'.format(nome, opção))

print('-------------------------------------------------------------')