from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Representa um restaurante com nome, categoria, status de atividade e avaliações.

    Attributes:
        restaurantes (list): Lista de todos os restaurantes criados.
    """

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Args:
            nome (str): O nome do restaurante.
            categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Retorna a representação em string do Restaurante.

        Returns:
            str: Nome e categoria do restaurante formatados.
        """
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """
        Imprime a lista de todos os restaurantes com seus detalhes.
        """
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação.".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Retorna o status de atividade do restaurante.

        Returns:
            str: '⌧' se ativo, '☐' se inativo.
        """
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        """
        Alterna o estado de atividade do restaurante entre ativo e inativo.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma avaliação e adiciona à lista de avaliações do restaurante.

        Args:
            cliente (str): O nome do cliente que está dando a avaliação.
            nota (int): A nota da avaliação.
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Calcula a média das avaliações do restaurante.

        Returns:
            float or str: A média das notas das avaliações ou '-' se não houver avaliações.
        """
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media