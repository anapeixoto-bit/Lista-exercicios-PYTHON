# ============================================================
# Exercício 16: Análise de Dados com Pandas
# ============================================================
import pandas as pd


def analisar_clientes(arquivo, renda_minima=5000):
    # 1. Carrega os dados
    df = pd.read_csv(arquivo)

    print("=== Análise de Clientes ===\n")
    print(f"Total de clientes: {len(df)}\n")

    # 2. Médias
    media_idade = df["Idade"].mean()
    media_renda = df["Renda"].mean()
    print(f"Média de idade : {media_idade:.1f} anos")
    print(f"Média de renda : R$ {media_renda:,.2f}\n")

    # 3. Cidade com mais clientes
    cidade_top = df["Cidade"].value_counts().idxmax()
    qtd_top    = df["Cidade"].value_counts().max()
    print(f"🏙️  Cidade com mais clientes: {cidade_top} ({qtd_top} clientes)\n")

    # 4. Clientes com renda acima do filtro
    filtrados = df[df["Renda"] > renda_minima]
    print(f"Clientes com renda acima de R$ {renda_minima:,.2f}:")
    print(filtrados[["Nome", "Cidade", "Renda"]].to_string(index=False))

    return df


if __name__ == "__main__":
    analisar_clientes("dados_clientes.csv", renda_minima=5000)
