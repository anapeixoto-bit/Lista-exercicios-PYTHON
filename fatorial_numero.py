#                     Fatorial de um Número 
# Desenvolva uma função recursiva para calcular o fatorial de um número inteiro positivo. 

#aprendendo fatorial 


def fatorial(n):
    if n <= 1:
        return n 
    else:
        return n * fatorial(n - 1)
    

print(fatorial(5))




