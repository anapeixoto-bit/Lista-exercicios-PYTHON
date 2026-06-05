#Calculadora Simples
#Desenvolva uma calculadora que peça dois números ao usuário e, em seguida, exiba a soma,
#subtração, multiplicação e divisão entre eles.


num1 = float(input('Diga-me um numero: '))
num2 = float(input('Diga-me outro numero: '))

soma = num1 + num2
divisao = num1 / num2
multiplicaçao = num1 * num2
sub = num1 - num2

print(f'A soma de {num1} e {num2} = {soma}  ')
print(f'A divisão de {num1} e {num2} = {divisao} ')
print(f'A multiplição de {num1} e {num2} = {multiplicaçao}  ')
print(f'A subtração de {num1} e {num2} = {sub} ')

