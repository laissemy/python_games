import sys
import random
from pathlib import Path
from typing import List
sys.path.append(str(Path(__file__).resolve().parent.parent))
from wordle_game.letterstate import LetterState
from wordle_game.wordle import Wordle
from colorama import Fore

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TEMAS = {
    "1": ("Ação", "acao.txt"),
    "2": ("Objeto", "objeto.txt"),
    "3": ("Comida", "comida.txt"),
    "4": ("Filme", "filme.txt"),
}

def main():
    
    escolha = escolher_opcao()

    if escolha:
        tema, arquivo = escolha
        word_set = load_set(DATA_DIR / arquivo)
        palavra_secreta = random.choice(list(word_set))
        iniciar_wordle(palavra_secreta, word_set,tema)
    else:
        print("Tchau")


def display_opcoes():
    opcoes = ["Escolha o tema da palavra:"]
    opcoes += [ f"{chave}.{nome}" for chave, (nome, _) in TEMAS.items()]
    opcoes.append("X.Sair")
    desenha_borda(opcoes, tamanho=max(len(o) for o in opcoes), centralizar=True)

def escolher_opcao():
    """Devolve tema e arquivo"""

    display_opcoes()
    
    while True:
        
        x = input(
                  Fore.LIGHTMAGENTA_EX
                  +  f"Insira o número: " 
                  + Fore.RESET
                  ).strip().upper()
        
        if x == "X":
            return None
        if x in TEMAS:
            return TEMAS[x]
        
        print(
            Fore.RED 
            + "Opção inválida, tente novamente." 
            + Fore.RESET
            )

def iniciar_wordle(palavra_secreta : str, word_set :str, tema : str):
    
    wordle = Wordle(palavra_secreta, tema)
    
    while wordle.possuiTentativas:
            
            display_resultados(wordle)
            tentativa = input(Fore.LIGHTMAGENTA_EX + "Escreva sua tentativa ou (x) para desistir: " + Fore.RESET).upper()

            if tentativa == "X":
                print(Fore.YELLOW + 
                      f"Fim de jogo" 
                      + Fore.RESET)
                break

            if (len(tentativa) != wordle.TAMANHO_PALAVRAS):
                print(
                        Fore.RED 
                      + f"A palavra deve ter {wordle.TAMANHO_PALAVRAS} caracteres"
                      + Fore.RESET
                      )
                continue 
    
            if not tentativa.upper() in word_set:
                print(
                    Fore.RED
                    + f"{tentativa} não é uma palavra válida!"
                    + Fore.RESET
                    )
                continue

            
                   
            
            wordle.tentativa(tentativa)
            display_resultados(wordle)

    if wordle.vitoria:
        print(
              Fore.GREEN 
              + f"Você acertou!" 
              + Fore.RESET
              )
    else:
        print(
              Fore.RED 
              + f"Você errou, a palavra era: {wordle.palavra_secreta}"
              + Fore.RESET
              )

def display_resultados(wordle : Wordle):

    linhas = []
    
    for palavra in wordle.tentativas:
        resultado = wordle.palpite(palavra)
        palavra_colorida = colorizador(resultado)
        linhas.append(palavra_colorida)

    for _ in range(wordle.tentativasRestantes):
        linhas.append(" ".join(["_"] * wordle.TAMANHO_PALAVRAS))

    desenha_borda(linhas=linhas)
    print(Fore.BLUE + f"Palavra possui: {wordle.TAMANHO_PALAVRAS} caracteres")
    print(f"Tentativas restantes: {wordle.tentativasRestantes}")
    print(f"Tema: {wordle.tema} \n" + Fore.RESET)

def load_set(path: str):
    
    word_set = set()
    
    with open(path, "r", encoding="utf-8") as f:
        for linha in f.readlines():
            palavra = linha.strip().upper()
            if palavra:
                word_set.add(palavra)
    return word_set

def colorizador(resultado : List[LetterState]):
    
    resultado_colorido = []
    
    for letra in resultado:
        cor = Fore.WHITE
        
        if letra.dentro_da_posicao:
            cor = Fore.GREEN
        elif letra.dentro_da_palavra:
            cor = Fore.YELLOW

        letra_cor = cor + letra.caractere + Fore.RESET
        resultado_colorido.append(letra_cor)
    return " ".join(resultado_colorido)

def desenha_borda(linhas : List[str], tamanho: int=9, pad: int=1, centralizar: bool=False):
    
    espacamento = tamanho + pad * 2
    borda_superior = "┌" + "─" * espacamento + "┐"
    borda_inferior = "└" + "─" * espacamento + "┘"
    espaco = " " * pad
    print(borda_superior)

    for linha in linhas:
        if centralizar:                      
            linha = linha.center(tamanho)    
        print("│" + espaco + linha + espaco + "│")

    print(borda_inferior)


if __name__ == "__main__":
    main()