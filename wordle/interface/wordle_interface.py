import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from wordle_game.wordle import Wordle


def main():
    print()
    wordle = Wordle("TESTE")

    while wordle.possuiTentativas:
        tentativa = input("Escreva sua tentativa: ")

        
        if (len(tentativa) < wordle.TAMANHO_PALAVRAS):
            print(f"Palavra menor do que {wordle.TAMANHO_PALAVRAS} caracteres")
        
        if (len(tentativa) > wordle.TAMANHO_PALAVRAS):
            print(f"Palavra maior do que {wordle.TAMANHO_PALAVRAS} caracteres")

        
        wordle.tentativa(tentativa)
        resultado = wordle.palpite(tentativa)
        print(*resultado, sep= "\n" )
    
    if wordle.vitoria:
        print("Você conseguiu!")
    else:
        print("Você perdeu!")


if __name__ == "__main__":
    main()