# ============================================================
# Exercício 15: Análise de Dados Simples (CSV)
# ============================================================
import csv
from collections import defaultdict


def analisar_vendas(arquivo):
    vendas_por_produto = defaultdict(lambda: {"quantidade": 0, "total": 0.0})

    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            produto    = linha["produto"]
            quantidade = int(linha["quantidade"])
            preco      = float(linha["preco"])

            vendas_por_produto[produto]["quantidade"] += quantidade
            vendas_por_produto[produto]["total"]      += quantidade * preco

    return vendas_por_produto


def main():
    print("=== Análise de Vendas ===\n")

    arquivo = "vendas.csv"
    vendas  = analisar_vendas(arquivo)

    total_geral      = 0.0
    mais_vendido     = None
    maior_quantidade = 0

    print(f"{'Produto':<12} {'Qtd':>6} {'Total':>12}")
    print("-" * 32)

    for produto, dados in vendas.items():
        qtd   = dados["quantidade"]
        total = dados["total"]
        total_geral += total
        print(f"{produto:<12} {qtd:>6} R$ {total:>9.2f}")

        if qtd > maior_quantidade:
            maior_quantidade = qtd
            mais_vendido     = produto

    print("-" * 32)
    print(f"{'TOTAL':<12}        R$ {total_geral:>9.2f}")
    print(f"\n Produto mais vendido: {mais_vendido} ({maior_quantidade} unidades)")


if __name__ == "__main__":
    main()
