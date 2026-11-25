"""Testes automatizados da função itens_disponiveis. Dados fictícios."""
import unittest

from diagnostico import itens_disponiveis


DADOS = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo HDMI", "quantidade": 5},
]


class ItensDisponiveis(unittest.TestCase):
    def test_limite_um_devolve_itens_com_estoque(self):
        self.assertEqual(
            itens_disponiveis(DADOS, 1),
            ["Notebook", "Cabo HDMI"],
        )

    def test_lista_vazia_retorna_lista_vazia(self):
        self.assertEqual(itens_disponiveis([], 1), [])

    def test_quantidade_igual_ao_limite_e_incluida(self):
        self.assertEqual(itens_disponiveis(DADOS, 3), ["Notebook", "Cabo HDMI"])

    def test_lista_recebida_nao_e_modificada(self):
        original = [registro.copy() for registro in DADOS]
        itens_disponiveis(DADOS, 1)
        self.assertEqual(DADOS, original)


if __name__ == "__main__":
    unittest.main()
