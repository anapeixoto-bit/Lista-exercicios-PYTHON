# ============================================================
# Exercício 19: Web Scraper Simples
# Dependências: pip install requests beautifulsoup4
# ============================================================
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_titulos(url, seletor_css, arquivo_saida="noticias.txt"):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return

    soup     = BeautifulSoup(resposta.text, "html.parser")
    elementos = soup.select(seletor_css)

    titulos = [el.get_text(strip=True) for el in elementos if el.get_text(strip=True)]

    if not titulos:
        print("Nenhum título encontrado. O seletor CSS pode estar desatualizado.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(f"Notícias coletadas em: {timestamp}\n")
        f.write(f"Fonte: {url}\n")
        f.write("=" * 50 + "\n")
        for i, titulo in enumerate(titulos[:20], 1):
            f.write(f"{i}. {titulo}\n")

    print(f"{len(titulos[:20])} títulos salvos em '{arquivo_saida}'.")
    for i, t in enumerate(titulos[:5], 1):
        print(f"  {i}. {t}")


def main():
    # BBC Brasil — seletor de títulos de notícias
    scrape_titulos(
        url          = "https://www.bbc.com/portuguese",
        seletor_css  = "h3",
        arquivo_saida= "noticias_bbc.txt",
    )


if __name__ == "__main__":
    main()
