class Cliente:
    def __init__(self, nome, contato, idade):
        self.nome = nome
        self.__contato = contato
        self.idade = idade 

    def get_contato(self):
        return self.__contato

    def set_contato(self, contato):
        if contato != self.__contato:
            self.__contato = contato
            print(f'Contato atualizado: {self.__contato} Obrigada!')

    def detalhes (self):
        print(f'Nome Cliente: {self.nome}')
        print(f'Idade Cliente: {self.idade}')
        print(f'Contato Cliente: {self.get_contato()}')

        
            
class Aluguel:
    def __init__(self, cliente, filme):
        self.preco = 0
        self.periodo = 0
        self.cliente = cliente
        self.filme = filme
    
    def devolucao (self, preco, periodo):
        periodo = int(input('Favor, digite quantos dias você ficou com o filme: '))
        if periodo >= 1:
            valor_por_dia = 2
            preco = periodo * valor_por_dia
            self.periodo = periodo
            self.preco = preco

    def dados_cliente(self):
        self.cliente.detalhes()

    def verificacao(self, filme):
        if self.cliente.idade < self.filme.classificacao:
            print('Você não possui a idade dentro da classificação do filme. Favor, escolher outro')



class Filme: 
    def __init__(self, nome, genero, ano_de_estreia,  sinopse, classificicacao ,diretor, produtora,):
        self.nome = nome
        self.genero = genero
        self.ano_de_estreia = ano_de_estreia
        self.diretor = diretor
        self.produtora = produtora
        self.sinopse = sinopse
        self.classificacao = classificicacao


class Produtora:
    def __init__(self, nome, diretores, filmes):
        self.nome = nome 
        self.diretores = diretores
        self.filmes = filmes 

    def detalhes(self):
        print(f'Nome Produtora: {self.nome} \n Nome diretores: {self.diretores} \n Filmes produzidos: {self.filmes}')


class Diretor:
    def __init__ (self, nome, produtoras, filmes):
        self.nome = nome
        self.produtoras = produtoras
        self.filmes = filmes
    
    def detalhes(self):
        print(f'Nome diretor: {self.nome} \n Produtas que trabalha: {self.produtoras} \n Filmes dirigidos: {self.filmes}')


cliente1 = Cliente('Joana', "11 972904999", 18)
cliente1.get_contato()
cliente1.set_contato('233478')

#deixei lindo, pode destruir :p

