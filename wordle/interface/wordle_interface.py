import sys
import random
from pathlib import Path
from typing import List
sys.path.append(str(Path(__file__).resolve().parent.parent))
from wordle_game.letterstate import LetterState
from wordle_game.wordle import Wordle
from colorama import Fore


def main():
    word_set = load_set("data/exemplo.txt")
    palavra_secreta = random.choice(list(word_set))
    wordle = Wordle(palavra_secreta)


    while wordle.possuiTentativas:
        display_resultados(wordle)

        tentativa = input(Fore.LIGHTCYAN_EX + "Escreva sua tentativa: " + Fore.RESET)
        
        if (len(tentativa) != wordle.TAMANHO_PALAVRAS):
            print(Fore.RED 
                  + f"A palavra deve ter {wordle.TAMANHO_PALAVRAS} caracteres"
                  + Fore.RESET)
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
        print(Fore.GREEN + "Você conseguiu!")
    else:
        print(Fore.RED + "Você perdeu!")



def display_resultados(wordle : Wordle):
    print(f"Palavra possui: {wordle.TAMANHO_PALAVRAS} caracteres")
    print(f"\n Tentativas restantes: {wordle.tentativasRestantes} \n")

    linhas = []
    
    for palavra in wordle.tentativas:
        resultado = wordle.palpite(palavra)
        palavra_colorida = colorizador(resultado)
        linhas.append(palavra_colorida)

    for _ in range(wordle.tentativasRestantes):
        linhas.append(" ".join(["_"] * wordle.TAMANHO_PALAVRAS))

    desenha_borda(linhas=linhas)

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

def desenha_borda(linhas : List[str], tamanho: int=9, pad: int=1):
    
    espacamento = tamanho + pad * 2
    borda_superior = "┌" + "─" * espacamento + "┐"
    borda_inferior = "└" + "─" * espacamento + "┘"
    espaco = " " * pad
    print(borda_superior)

    for linha in linhas:
        print("│" + espaco + linha + espaco + "│")

    print(borda_inferior)

def load_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for linha in f.readlines():
            palavra = linha.strip().upper()
            word_set.add(palavra)
    return word_set

if __name__ == "__main__":
    main()