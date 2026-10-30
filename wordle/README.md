# Wordle no Terminal

Uma implementação em Python do jogo **Wordle** para jogar direto no terminal, com palavras em português.

Feito com inspiração neste [vídeo tutorial](https://www.youtube.com/watch?v=SyWeex-S6d0&t=890s).

## Regras

- O objetivo do jogo é achar a **palavra secreta de 5 letras**.
- O jogador tem ao todo **6 tentativas**.
- A cada tentativa, o jogador deve digitar uma palavra válida de 5 letras.
- Depois de cada palpite, as letras ganham uma cor:

| Cor | Significado |
|-----|-------------|
| 🟩 **Verde** | A letra existe na palavra e está na posição correta |
| 🟨 **Amarelo** | A letra existe na palavra, mas em outra posição |
| ⬜ **Branco** | A letra não existe na palavra |

- Se o jogador acertar a palavra, vence. Se as tentativas acabarem, perde.

### Exemplo

Palavra secreta: `TERRA`

```
Escreva sua tentativa: TARDE

T  (verde)    → posição certa
A  (amarelo)  → existe, mas em outro lugar
R  (verde)    → posição certa
D  (branco)   → não existe
E  (amarelo)  → existe, mas em outro lugar
```

## Como jogar:

### 1. Clone o repositório

```bash
git clone https://github.com/laislirah/python_games.git
cd python_games/wordle
```

### 2. Instale as dependências

Confira as bibliotecas necessárias em `requirements.txt` e instale com:

```bash
pip install -r requirements.txt
```

### 3. Execute o jogo

Dentro da pasta raiz `wordle/`, rode:

```bash
python interface/wordle_interface.py
```

## Estrutura do projeto

```
wordle/
├── data/
│   └── exemplo.txt           # Palavras usadas no jogo
├── interface/
│   └── wordle_interface.py   # Interface e loop do jogo no terminal
├── wordle_game/
│   ├── wordle.py             # Lógica principal do jogo
│   └── letterstate.py        # Estado de cada letra (posição, presença)
├── requirements.txt          # Dependências do projeto
└── README.md
```

## Feito com
- [Python 3](https://www.python.org/)
- [Colorama](https://pypi.org/project/colorama/): cores no terminal

## Melhorias futuras

- [ ] Validar se o palpite existe na lista de palavras
- [ ] Tratar acentos na entrada do jogador
- [ ] Mostrar o teclado com as letras já usadas
- [ ] Contador de vitórias e derrotas


feito por [@laissemy](https://github.com/laissemy).