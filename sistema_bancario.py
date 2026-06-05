# ============================================================
# Exercício 17: Sistema Bancário (POO)
# ============================================================


class ContaBancaria:
    _contador = 1000  # numeração automática

    def __init__(self, titular):
        ContaBancaria._contador += 1
        self.numero_conta = ContaBancaria._contador
        self.titular      = titular
        self.saldo        = 0.0

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")

    def verificar_saldo(self):
        print(f"Conta {self.numero_conta} | {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def __str__(self):
        return f"Conta {self.numero_conta} ({self.titular}) - R$ {self.saldo:.2f}"


class Cliente:
    def __init__(self, nome, cpf):
        self.nome   = nome
        self.cpf    = cpf
        self.contas = []

    def abrir_conta(self):
        conta = ContaBancaria(titular=self.nome)
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} aberta para {self.nome}.")
        return conta

    def listar_contas(self):
        if not self.contas:
            print(f"{self.nome} não possui contas.")
            return
        print(f"\nContas de {self.nome}:")
        for c in self.contas:
            print(f"  {c}")

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


class Banco:
    def __init__(self, nome):
        self.nome     = nome
        self.clientes = []

    def adicionar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente '{nome}' cadastrado no {self.nome}.")
        return cliente

    def buscar_conta(self, numero_conta):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    return conta
        print(f"Conta {numero_conta} não encontrada.")
        return None

    def listar_clientes(self):
        print(f"\n=== Clientes do {self.nome} ===")
        for c in self.clientes:
            print(f"  {c}")


# ── Demonstração ──────────────────────────────────────────
def main():
    banco = Banco("Banco Python")

    # Cadastro de clientes
    ana    = banco.adicionar_cliente("Ana Lima",    "529.982.247-25")
    carlos = banco.adicionar_cliente("Carlos Silva", "111.444.777-35")

    # Abertura de contas
    conta_ana    = ana.abrir_conta()
    conta_carlos = carlos.abrir_conta()
    conta_ana2   = ana.abrir_conta()   # Ana tem duas contas

    print()

    # Operações
    conta_ana.depositar(1500)
    conta_ana.sacar(200)
    conta_ana.verificar_saldo()

    print()
    conta_carlos.depositar(3000)
    conta_carlos.sacar(5000)   # saldo insuficiente
    conta_carlos.verificar_saldo()

    # Busca por número
    print()
    banco.buscar_conta(conta_ana.numero_conta).verificar_saldo()

    # Listagens
    banco.listar_clientes()
    ana.listar_contas()


if __name__ == "__main__":
    main()
