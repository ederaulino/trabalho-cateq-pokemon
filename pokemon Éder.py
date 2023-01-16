import random #Biblioteca de funções de aleatoriedade

#Requisito 1 - Modelar classe pokemon com uma série de atributos

class Pokemon:  
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        self._nome = nome 
        self._especie = especie 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Movimento de ataque"

#Requisito 2 - Criar 3 subclasses de Pokemon com base em seu tipo

class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
    
        self._tipo = "aquatico"
        self._movimento = "Jato de água"

class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "fogo"
        self._movimento = "Lança chamas"

class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "grama"
        self._movimento = "Chicote de cipó"

class Psiquico(Pokemon):
    def _init_(self, nome, tipo, hp, level):
        super()._init_(nome, tipo, hp, level)
        self._tipo = "Psiquico"
        self._movimento = "Controle da mente"

class Lutador(Pokemon):
    def _init_(self, nome, tipo, hp, level):
        super()._init_(nome, tipo, hp, level)
        self._tipo = "Lutador"
        self._movimento = "Chute duplo"

#Requisito 3 - Modelar classe Treinador
class Treinador: 
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

#Requisito 4 - Modelar as subclasses Jogador e Inimigo
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

#Esse método permite que o jogador escolha um Pokemon de sua lista para batalhar
    def escolherPokemon(self): 
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")

#Requisito 6  - Essa função captura o pokemon

    def capturarPokemon(self, pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")

# Requisito 7 - Essa função lista todos os pokemons 
    def listarPokemons(self): 
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

       
class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)


#Requisito 5 - Método de batalha
    
def batalhaPokemon(treinador1, treinador2):

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Forca = p1._ataque + p1._defesa + p1._hp
    p2Forca = p2._ataque + p2._defesa + p2._hp

#Vantagem de tipo em 50% em cima do dano básico da Força do Pokemon

    if (p1._tipo == Fogo) and (p2._tipo == Grama):
        p1Forca*1.5
    elif (p1._tipo == Aquatico) and (p2._tipo == Fogo):
        p1Forca*1.5
    elif (p1._tipo == Grama) and (p2._tipo == Aquatico):
        p1Forca*1.5
    elif (p1._tipo == Psiquico) and (p2._tipo == Lutador):
        p1Forca*1.5

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e forca {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")

pokemonsDisponiveis = [
Fogo("Charmander", "Charmander", "Fogo", 100,50,50),
Grama("Bulbasauro", "Bulbasauro", "Grama",200,50,50),
Aquatico("Squirtle", "Squirtle", "Aquatico",300,50,50),
Fogo("Charmeleon", "Charmeleon", "Fogo", 200, 100, 100),
Grama("Ivysauro", "Ivysauro", "Grama",300,50,50),
Aquatico("Wartortle", "Wartortle", "Aquatico",300,100,50),
Psiquico("Abra", "Abra", "Psiquico", 220, 150, 100),
Lutador("Machop", "Machop", "Lutador", 150, 200, 80),
]

#Requisito opcional: Criar um menu para o jogador

nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(3):
    print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

pokemonInicial = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]

print(f"O pokemon escolhido foi o {pokemonInicial._nome}")

jogador = Jogador(nomeJogador, [pokemonInicial])
inimigo = Inimigo("Bob", pokemonsDisponiveis)

while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    0. Sair do jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Você saiu do jogo.")
        break
    elif menu=="1":
        jogador.listarPokemons()
    elif menu=="2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")
        
        capturado = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu=="3":
        batalhaPokemon(jogador,inimigo)
    else:
        print("Você digitou algo inválido, tente novamente.")


    

