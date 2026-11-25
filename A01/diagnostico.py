"""A01 — Diagnóstico de equipamentos. Todos os dados são fictícios."""


def itens_disponiveis(equipamentos, limite):
    """Retorna nomes com quantidade >= limite, preservando a ordem original.

    A lista recebida não é modificada.
    """
    disponiveis = []
    for equipamento in equipamentos:
        if equipamento["quantidade"] >= limite:
            disponiveis.append(equipamento["nome"])
    return disponiveis


equipamentos = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo HDMI", "quantidade": 5},
]


if __name__ == "__main__":
    for registros, limite in [(equipamentos, 1), (equipamentos, 4), ([], 1)]:
        resultado = itens_disponiveis(registros, limite)
        print(f"Limite {limite} => {resultado}")
