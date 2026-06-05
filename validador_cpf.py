
# Exercício 14: Validador de CPF

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = "".join(c for c in cpf if c.isdigit())

    # Deve ter exatamente 11 dígitos e não ser sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação do 1º dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Validação do 2º dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True


def main():
    print("=== Validador de CPF ===\n")

    testes = [
        "529.982.247-25",   # válido
        "111.111.111-11",   # inválido (sequência)
        "123.456.789-09",   # inválido
        "000.000.000-00",   # inválido (sequência)
    ]

    for cpf in testes:
        resultado = "VÁLIDO" if validar_cpf(cpf) else " INVÁLIDO"
        print(f"CPF {cpf}: {resultado}")

    print()
    cpf_usuario = input("Digite um CPF para validar: ")
    resultado = "VÁLIDO" if validar_cpf(cpf_usuario) else "INVÁLIDO"
    print(f"CPF {cpf_usuario}: {resultado}")

