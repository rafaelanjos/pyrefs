import heapq

class FilaDePrioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1
    
    def remover(self):
        return heapq.heappop(self.fila)[-1]

class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome
        #return f'{self.nome}'
        #return '%s'.format(self.nome)

if __name__ == '__main__':
    fila = FilaDePrioridade()
    fila.inserir(Item('Marcos'), 28)
    fila.inserir(Item('Joao'), 30)
    fila.inserir(Item('Maria'), 18)

    print(fila.remover())
    print(fila.remover())