from wordle_game.letterstate import LetterState

class Wordle:
    NUM_TENTATIVAS = 6
    TAMANHO_PALAVRAS = 5

    def __init__(self, palavra_secreta : str):
        self.palavra_secreta : str = palavra_secreta.upper()
        self.tentativas = []
        pass


    def tentativa(self, tentativa : str):
        self.tentativas.append(tentativa.upper())

    @property
    def tentativasRestantes(self) -> int:
        return self.NUM_TENTATIVAS - len(self.tentativas)

    @property
    def possuiTentativas(self):
        return self.tentativasRestantes >= 0 and not self.vitoria
    
    @property
    def vitoria(self):
        return len(self.tentativas) > 0  and self.tentativas[-1] == self.palavra_secreta
   
    def palpite(self, palavra : str ):
        palavra = palavra.upper()
        resultado = []

        for i in range(self.TAMANHO_PALAVRAS):
            letra = LetterState(palavra[i])
            letra.dentro_da_palavra = palavra[i] in self.palavra_secreta
            letra.dentro_da_posicao = palavra[i] == self.palavra_secreta[i]
            resultado.append(letra)
        return resultado

