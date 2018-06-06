class ListaSeq:
    "Lista Estatica Sequencial"
    def __init__(self):
        self.dados = []
    def insert(self, x):
        if self.size() == 0:
            self.dados.append(x)
        else:
            for i in range(self.size()):
                if x >= self.dados[i]:
                    self.dados[i-1] = x
                    #pass
    def remove(self,x):
        for i in range(self.size()):
            if x == self.dados[i]:
                self.dados.pop(i)
    def size(self):
        return len(self.dados)
    def print(self):
        return print(self.dados)

lista = ListaSeq()
lista.insert(3)
lista.insert(2)
lista.insert(1)
lista.insert(8)
lista.insert(5)
lista.print()