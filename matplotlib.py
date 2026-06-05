# ============================================================
# Exercício 18: Visualização de Dados com Matplotlib
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt


def graficos(arquivo):
    df = pd.read_csv(arquivo)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Análise de Clientes", fontsize=14, fontweight="bold")

    # --- Gráfico 1: Clientes por cidade ---
    contagem = df["Cidade"].value_counts()
    ax1.bar(contagem.index, contagem.values, color="steelblue", edgecolor="white")
    ax1.set_title("Clientes por Cidade")
    ax1.set_xlabel("Cidade")
    ax1.set_ylabel("Número de Clientes")
    ax1.tick_params(axis="x", rotation=20)

    # --- Gráfico 2: Histograma de idades ---
    ax2.hist(df["Idade"], bins=6, color="salmon", edgecolor="white")
    ax2.set_title("Distribuição de Idades")
    ax2.set_xlabel("Idade")
    ax2.set_ylabel("Frequência")

    plt.tight_layout()
    plt.savefig("graficos_clientes.png", dpi=150)
    print("Gráfico salvo em 'graficos_clientes.png'.")
    plt.show()


if __name__ == "__main__":
    graficos("dados_clientes.csv")
