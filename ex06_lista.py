#Lista de Compras 
# Crie um programa que permita ao usuário adicionar, remover e visualizar itens de uma lista de compras. Utilize uma lista para armazenar os itens. 


def adcionar(lista):
    item = input('Digite o que voçe quer adcionar: ')
    lista.append(item)
    print('Item adcionado')

    return lista

def remover(lista):
    item = input('O que voçe quer remover? ')
    if item in lista:
     lista.remove(item)
     print(f'Esse {item} foi removido')
    else:
      print('Item não encontrado')

    return lista


#def visualizar(lista):
    for item in lista:
     print(f'Sua lista tem: {item}')
     
    return


lista1 = []

while True:
  
    print('    LISTA DE COMPRAS    \n')
    print('        MENU          ')
    print(' 1=Adcionar itens     ')
    print(' 2=Remover itens      ')
    print(' 3=Ver lista   ')

    opção = int(input('Escolha a opção: '))
   

    if opção == 1:
     lista1 = adcionar(lista1)
     
    elif opção == 2:
     lista1 = remover(lista1)
     
    elif opção == 3:
     for item in lista1:
       print(f'Sua lista tem: {item}')
   
    else:
     print('Algo deu errado!Tente voltar ao menu')
     break
    



############################################## em logica de programação o while vem no final.



    




    
    

