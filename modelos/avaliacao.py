class Avaliacao:
    """
    Representa uma avaliação feita por um cliente a um restaurante.

    Attributes:
       _cliente (str): O nome do cliente que fez a avaliação.
       _nota (int): A nota dada pelo cliente ao restaurante.
    """
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
        
