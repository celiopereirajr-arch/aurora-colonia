# dados.py
# Desenvolvido com apoio da ferramenta de IA Claude (ver declaração no README).
# Guarda e organiza os dados da colônia Aurora Siger.
# Aqui só existem dados e funções de leitura. Nenhuma decisão é tomada.

# Histórico de sensores (listas): vento medido e energia eólica gerada.
VENTO_HIST = [8, 10, 12]
ENERGIA_HIST = [20, 25, 30]


def criar_colonia():
    """Monta a colônia como dicionários dentro de dicionários (hierarquia)."""
    colonia = {
        "energetico": {
            "solar": {"geracao": 25},
            "eolico": {"geracao": 20},
            "baterias": {"carga": 60},
        },
        "ambiental": {
            "vento": 11,
            "temp_externa": -60,
            "temp_interna": 20,
        },
        "operacional": {
            "suporte_vida": {"consumo": 20, "essencial": True},
            "comunicacao": {"consumo": 10, "essencial": True},
            "laboratorio": {"consumo": 10, "essencial": False},
        },
    }
    return colonia


def geracao_total(colonia):
    """Soma a geração das fontes de energia (solar + eólico)."""
    fontes = colonia["energetico"]
    return fontes["solar"]["geracao"] + fontes["eolico"]["geracao"]


def consumo_total(colonia):
    """Soma o consumo de todos os módulos operacionais."""
    total = 0
    for nome in colonia["operacional"]:
        total = total + colonia["operacional"][nome]["consumo"]
    return total


if __name__ == "__main__":
    c = criar_colonia()
    print("Solar:", c["energetico"]["solar"]["geracao"])
    print("Geração total:", geracao_total(c))
    print("Consumo total:", consumo_total(c))
