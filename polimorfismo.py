from abc import ABC, abstractmethod

#criando um metodo abstrato para um controle remoto universal

class ControleUniversal(ABC):
    def __init__(self, marca, comodo):
        self.marca = marca
        self.comodo = comodo
        self.status = False

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def volume(self, volume):
        pass



class Tv(ControleUniversal):

    def __init__(self, marca, comodo):
        super().__init__(marca, comodo)
        print(f'Tv {marca}, esta no comodo {comodo}')

    def ligar(self):
        self.status = True   
        print('Ligando')

    def desligar(self):
        self.status = False
        print('Desligando')

    def volume(self, volume):
        if volume == '+':
            print('Aumentando volume')
        elif volume == '-':
            print('Diminuindo volume')
    
    def canal(self, tecla):
        self.tecla = tecla
        print(f'Mudando para canal {tecla}')
        
class Som(ControleUniversal):
    def __init__(self, marca, comodo):
        super().__init__(marca, comodo)
        print(f'Aparelho de som {marca}, esta no comodo {comodo}')    

    def ligar(self):
        self.status = True
        print('Ligando')


    def desligar(self):
        self.status = False
        print('Desligando')

    def volume(self, volume):
        if volume == '+':
            print('Aumentando volume')
        elif volume == '-':
            print('Diminuindo volume')

Tv_quarto = Tv('samsung', 'quarto')
Som_sala = Som('LG', 'sala')
print('\nTV') 
Tv_quarto.ligar()
Tv_quarto.volume('+')
Tv_quarto.canal('10')
Tv_quarto.desligar()
print('\nSOM') 
Som_sala.ligar()
Som_sala.volume('-')
Som_sala.desligar()