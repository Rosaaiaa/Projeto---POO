from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, cpf, nome, idade, contato, endereco):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.contato = contato
        self.endereco = endereco

# Classe Diretor
class Diretor:
    def __init__(self, nome_diretor):
        self.nome_diretor = nome_diretor
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def consultar_filmes(self):
        return [filme.nome_filme for filme in self.filmes]

# Classe Produtora
class Produtora:
    def __init__(self, nome_produtora):
        self.nome_produtora = nome_produtora
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def consultar_filmes(self):
        return [filme.nome_filme for filme in self.filmes]

# Classe Filme
class Filme:
    def __init__(self, nome_filme, genero, ano_estreia, classificacao, sinopse, diretor, produtora):
        self.nome_filme = nome_filme
        self.genero = genero
        self.ano_estreia = ano_estreia
        self.classificacao = classificacao
        self.sinopse = sinopse
        self.diretor = diretor
        self.produtora = produtora

        # Associa o filme ao diretor e à produtora
        diretor.adicionar_filme(self)
        produtora.adicionar_filme(self)

# Classe Aluguel
class Aluguel:
    def __init__(self, id_aluguel, preco, tempo_aluguel, cliente, filme):
        self.id_aluguel = id_aluguel
        self.preco = preco
        self.tempo_aluguel = tempo_aluguel
        self.data_aluguel = datetime.now()
        self.cliente = cliente
        self.filme = filme

    def devolver(self):
        print(f"Filme '{self.filme.nome_filme}' devolvido pelo cliente {self.cliente.nome}.")

def função():
    pass
print(função)