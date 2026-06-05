# Lista de Compras

def adicionar(lista):
    item = input('Digite o que você quer adicionar: ')
    lista.append(item)
    print(f'"{item}" adicionado com sucesso!')
    return lista

def remover(lista):
    item = input('O que você quer remover? ')
    if item in lista:
        lista.remove(item)
        print(f'"{item}" foi removido.')
    else:
        print('Item não encontrado na lista.')
    return lista

lista1 = []

while True:
    print('\n    LISTA DE COMPRAS    ')
    print('        MENU          ')
    print(' 1 = Adicionar itens  ')
    print(' 2 = Remover itens    ')
    print(' 3 = Ver lista        ')
    print(' 4 = Sair             ')

    try:
        opcao = int(input('Escolha a opção: '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if opcao == 1:
        lista1 = adicionar(lista1)

    elif opcao == 2:
        lista1 = remover(lista1)

    elif opcao == 3:
        if lista1:
            print('\nItens na lista:')
            for item in lista1:
                print(f'  - {item}')
        else:
            print('Sua lista está vazia!')

    elif opcao == 4:
        print('Encerrando o programa. Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente.')





    




    
    

