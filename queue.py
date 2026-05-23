class Queue:
    """
    Classe que representa uma fila FIFO (First In, First Out).
    """

    def __init__(self, max_size=None):
        """
        Inicializa uma fila vazia.

        :param max_size: tamanho máximo da fila (opcional).
                         None significa fila ilimitada.
        """
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        """
        Adiciona um item no final da fila.

        :param item: item a ser adicionado.
        :raises OverflowError: se a fila estiver cheia.
        """
        if self.is_full():
            raise OverflowError("Erro: a fila está cheia.")

        self.items.append(item)

    def dequeue(self):
        """
        Remove e retorna o primeiro item da fila.

        :return: primeiro item da fila.
        :raises IndexError: se a fila estiver vazia.
        """
        if self.is_empty():
            raise IndexError("Erro: a fila está vazia.")

        return self.items.pop(0)

    def peek(self):
        """
        Retorna o primeiro item sem removê-lo.

        :return: primeiro item da fila.
        :raises IndexError: se a fila estiver vazia.
        """
        if self.is_empty():
            raise IndexError("Erro: a fila está vazia.")

        return self.items[0]

    def is_empty(self):
        """
        Verifica se a fila está vazia.

        :return: True se vazia, False caso contrário.
        """
        return len(self.items) == 0

    def is_full(self):
        """
        Verifica se a fila está cheia.

        :return: True se cheia, False caso contrário.
        """
        if self.max_size is None:
            return False

        return len(self.items) >= self.max_size

    def size(self):
        """
        Retorna a quantidade de elementos na fila.

        :return: número de elementos.
        """
        return len(self.items)

    def clear(self):
        """
        Remove todos os elementos da fila.
        """
        self.items.clear()