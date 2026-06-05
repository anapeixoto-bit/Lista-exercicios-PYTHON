# ============================================================
# Exercício 20: Jogo da Forca (POO)
# ============================================================
import random


class Palavra:
    BANCO = [
        ("python",      "linguagem de programação"),
        ("computador",  "equipamento eletrônico"),
        ("algoritmo",   "sequência de passos lógicos"),
        ("internet",    "rede mundial de computadores"),
        ("programacao", "ato de escrever código"),
        ("variavel",    "espaço na memória para guardar valor"),
        ("funcao",      "bloco de código reutilizável"),
    ]

    def __init__(self):
        self.texto, self.dica = random.choice(self.BANCO)

    def revelar(self, letras_certas):
        return " ".join(l if l in letras_certas else "_" for l in self.texto)

    def completa(self, letras_certas):
        return all(l in letras_certas for l in self.texto)


class Jogador:
    def __init__(self, nome):
        self.nome         = nome
        self.letras_erradas = []
        self.letras_certas  = set()

    def adivinhar(self, letra, palavra_texto):
        if letra in palavra_texto:
            self.letras_certas.add(letra)
            return True
        else:
            if letra not in self.letras_erradas:
                self.letras_erradas.append(letra)
            return False

    @property
    def erros(self):
        return len(self.letras_erradas)


class Jogo:
    MAX_ERROS = 6
    FORCA = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
    ]

    def __init__(self):
        self.palavra = Palavra()
        nome = input("Qual é o seu nome? ").strip() or "Jogador"
        self.jogador = Jogador(nome)

    def exibir_estado(self):
        print(self.FORCA[self.jogador.erros])
        print(f"\nDica: {self.palavra.dica}")
        print(f"Palavra: {self.palavra.revelar(self.jogador.letras_certas)}")
        print(f"Letras erradas: {', '.join(self.jogador.letras_erradas) or '-'}")
        print(f"Tentativas restantes: {self.MAX_ERROS - self.jogador.erros}\n")

    def pedir_letra(self):
        todas = set(self.jogador.letras_certas) | set(self.jogador.letras_erradas)
        while True:
            letra = input("Digite uma letra: ").lower().strip()
            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas uma letra.")
            elif letra in todas:
                print("Você já tentou essa letra.")
            else:
                return letra

    def jogar(self):
        print("\n=== JOGO DA FORCA ===")
        while True:
            self.exibir_estado()

            if self.palavra.completa(self.jogador.letras_certas):
                print(f" Parabéns, {self.jogador.nome}! Você venceu!")
                print(f"A palavra era: {self.palavra.texto}")
                break

            if self.jogador.erros >= self.MAX_ERROS:
                print(f" Você perdeu, {self.jogador.nome}.")
                print(f"A palavra era: {self.palavra.texto}")
                break

            letra = self.pedir_letra()
            acertou = self.jogador.adivinhar(letra, self.palavra.texto)
            print(" Acertou!" if acertou else " Errou!")


def main():
    while True:
        jogo = Jogo()
        jogo.jogar()
        novamente = input("\nJogar novamente? (s/n): ").lower()
        if novamente != "s":
            print("Até logo!")
            break


if __name__ == "__main__":
    main()
