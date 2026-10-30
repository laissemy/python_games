class LetterState:
    
    def __init__(self, caractere : str):
        self.caractere = caractere
        self.dentro_da_palavra = False
        self.dentro_da_posicao = False

    def __repr__(self):
        return f"[{self.caractere} Letra dentro da palavra: {self.dentro_da_palavra} Letra na posição certa: {self.dentro_da_posicao}]"