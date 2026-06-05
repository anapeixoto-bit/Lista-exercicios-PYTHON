# Conversor de temperatura
def converção(origem,graus):
    if origem == 'C':
        calculo = (graus * 1.8) + 32
    elif origem == 'F':
        calculo = (graus - 32) *5/9

    return calculo
        
    
print("\n\n=== CONVERSOR DE TEMPERATURA ===")
print('\n')


opcao = str(input('A temperatura atual está em C(elsius) F(ahrenheit)?  ')).upper()
graus = float(input('Quantos graus? '))
if opcao == 'C':
    celsius = converção(opcao, graus)
    print(f'Sua temperatura em Fahrenheit é {celsius}')
elif opcao == 'F':
    fahrenheit = converção(opcao, graus)
    print(f'Sua temperatura em Celsius é {fahrenheit}')
else:
    print('Algo deu errado!')
# Converter celsius para fahrenheit e vice-versa, deve perguntar para qual temperatura deve converterde


    