class Cliente:
    def __init__(self, nome, contato, idade):
        self.nome = nome
        self.__contato = contato
        self.idade = idade 

    def get_contato(self):
        print(f'Telefone para contato: {self.__contato}')

    def set_contato(self, contato):
        if contato != self.__contato:
            self.__contato = contato
            print(f'Contato atualizado: {self.__contato} Obrigada!')

    def detalhes (self):
        print(f'Nome Cliente: {self.nome}')
        print(f'Idade Cliente: {self.idade}')

        
            
class Aluguel(Cliente):
    def __init__(self, nome, idade, contato, preco, tempo):
        super().__init__(nome, idade, contato)
        self.preco = preco
        self.tempo = tempo

    def periodo_aluguel (self, tempo):
        tempo = int(input(f'Escolha um período de tempo para alugar seu filme: \n1. 7 dias \n2. 15 dias \n3. 1 mês'))
        if tempo == 1:
            print('Seu filme foi alugado por 7 dias!')
            self.tempo = tempo
        if tempo == 2:
            print('Seu filme foi alugado por 15 dias!')
            self.tempo = tempo
        if tempo == 3:
            print('Seu filme foi alugado por 1 mês!')
            self.tempo = tempo    
   
        
#Fiquei com algumas dúvidas em relação a como adicionar o filme, acho melhr discutirmmos sobre :p











'''

class Produtora:

class Diretor:
'''
cliente1 = Cliente('Joana', "11 972904999", 18)
cliente1.get_contato()
cliente1.set_contato('233478')