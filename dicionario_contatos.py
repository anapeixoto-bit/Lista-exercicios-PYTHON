#dicionario de contas
#Crie um projeto que gerencie uma lista de contatos.Cada contato deve ter nome, telefone e email, armazenados em um dicionario
#permita adcionar,buscar e listar contatos.

    
lista_contatos = {}

while True:
  
    print('    LISTA DE CONTADOS   \n')
    print('        MENU            ')
    print(' 1=ADCIONAR contato     ')
    print(' 2=BUSCAR contato      ')
    print(' 3=LISTAR contato      ')
    print(' 4=SAIR                ')

    opção = int(input('Escolha a opção: '))

    if opção == 1:
        nome = input('Digite o nome do contato? ').lower()
        telefone = input('TELEFONE: ').lower()
        email = input('EMAIL: ').lower()

        #salvando dados 
        lista_contatos[nome] = {'telefone': telefone , 'email': email}
        print('Contato adcionado')
        

    elif opção == 2:
        buscar = input('Qual o nome do contato para buscar: ').lower()
       
        if buscar in lista_contatos:
            
            print(f'NOME : {buscar}')
            print(f'TELEFONE : {lista_contatos[buscar]['telefone']}')
            print(f'EMAIL: {lista_contatos[buscar]['email']}')
        
        else:
           print('Contato não existente')
    

    elif opção == 3:
        for nome, dados in lista_contatos.items(): 
         print(f'Contatos').upper()
         print(f'\n{nome}, {dados}')

    elif opção == 4:
       print('Voçe saiu!')
       break
    
    else:
        print('Algo deu errado!')
        break



   
     



    
