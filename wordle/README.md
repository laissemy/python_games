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
│   ├── acao.txt              # Palavras do tema Ação
│   ├── objeto.txt            # Palavras do tema Objeto
│   ├── comida.txt            # Palavras do tema Comida
│   └── filme.txt             # Palavras do tema Filme
├── interface/
│   └── wordle_interface.py   # Interface e loop do jogo no terminal
├── wordle_game/
│   ├── wordle.py             # Lógica principal do jogo
│   └── letterstate.py        # Estado de cada letra (posição, presença)
├── requirements.txt          # Dependências do projeto
└── README.md
```

## Adicionando novos temas

Cada tema é um arquivo `.txt` dentro da pasta `data/`. Para criar o seu:

### 1. Crie o arquivo de palavras

Crie um arquivo em `data/`, por exemplo `animal.txt`, seguindo estas regras:

- Uma palavra por linha.
- Todas as palavras com **5 letras**.
- Sem acentos (por exemplo, `agua` e não `água`).
- Sem linhas com outro conteúdo (título, comentários etc.).

Exemplo de `animal.txt`:

```
zebra
tigre
cobra
ovelha
```

### 2. Registre o tema no código

Abra `interface/wordle_interface.py` e adicione uma linha no dicionário `TEMAS`, com o número da opção, o nome que aparece no menu e o nome do arquivo:

```python
TEMAS = {
    "1": ("Ação", "acao.txt"),
    "2": ("Objeto", "objeto.txt"),
    "3": ("Comida", "comida.txt"),
    "4": ("Filme", "filme.txt"),
    "5": ("Animal", "animal.txt"),   # novo tema
}
```

O menu é montado a partir desse dicionário, então a nova opção aparece sozinha na próxima vez que você rodar o jogo.

## Feito com

- [Python 3](https://www.python.org/)
- [Colorama](https://pypi.org/project/colorama/): cores no terminal

## Melhorias futuras

- [ ] Tratar acentos na entrada do jogador
- [ ] Mostrar o teclado com as letras já usadas
- [ ] Contador de vitórias e derrotas

## Autora

Feito por [@laissemy](https://github.com/laissemy).