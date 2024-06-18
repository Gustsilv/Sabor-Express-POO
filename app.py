from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gusta', 3)
restaurante_praca.receber_avaliacao('Nanda', 4)
restaurante_praca.receber_avaliacao('Ana', 4)
restaurante_praca.receber_avaliacao('Italo', 3)



def main():
    Restaurante.listar_restaurantes()
    """
    Função principal que executa o programa.
    """
if __name__ == '__main__':
    main()
