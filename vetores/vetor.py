class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def tamanhoVetor(self):
        return len(self.__elementos)

    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])

    def contem(self, elemento):
        #1 2 4 3
        for i in range(self.tamanhoVetor()):
            elem = self.listar_elementos(i)
            if elem == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanhoVetor()):
            elem = self.listar_elementos(i)
            if elem == elemento:
                return i
        return -1

    def inserir_elemento_posicoes(self, elemento, posicao):
        #1 ,2, 3
        #inserir elemento posição (3,1)
        vetorIncio = self.__elementos[:posicao] + [None]
        vetorFinal = self.__elementos[posicao:]
        vetorIncio[len(vetorIncio) - 1] = elemento
        self.__elementos = vetorIncio + vetorFinal
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        # 1, 2
        # 2
        if self.__posicao >= self.tamanhoVetor():
            self.__elementos = self.__elementos + [None]

        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elementos(self, posicao):
        return self.__elementos[posicao]
