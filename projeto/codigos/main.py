# main.py
# Ponto de entrada do sistema da colônia Aurora Siger.
# Junta os dados (dados.py), as decisões (decisoes.py) e a previsão (previsao.py).
# Para rodar: python main.py

from dados import (VENTO_HIST, ENERGIA_HIST, criar_colonia,
                   geracao_total, consumo_total)
from decisoes import decidir_energia, analisar_uso, modo_economia, MSG_CRITICO
from previsao import prever_energia


def mostrar_exemplos_do_enunciado():
    """Mostra os exemplos de entrada e saída pedidos no enunciado."""
    print("EXEMPLOS DO ENUNCIADO")
    print("energia 40, consumo 70   ->", decidir_energia(40, 70))
    print("geração 40, consumo 70   ->", analisar_uso(40, 70))
    print("geração 80, consumo 30   ->", analisar_uso(80, 30))
    previsao, aviso = prever_energia(11, VENTO_HIST, ENERGIA_HIST)
    print("vento 11                 -> energia prevista", previsao)
    print()


def avaliar_colonia(nome, colonia, vento):
    """Lê os dados, prevê a energia eólica, decide e mostra a ação."""
    bateria = colonia["energetico"]["baterias"]["carga"]
    solar = colonia["energetico"]["solar"]["geracao"]
    geracao = geracao_total(colonia)
    consumo = consumo_total(colonia)

    eolico_previsto, aviso = prever_energia(vento, VENTO_HIST, ENERGIA_HIST)
    geracao_prevista = solar + eolico_previsto
    previsao_ruim = geracao_prevista < consumo

    print("CENÁRIO:", nome)
    print("  bateria", bateria, " geração", geracao, " consumo", consumo,
          " vento", vento)
    print("  previsão: eólico", eolico_previsto,
          " geração prevista", geracao_prevista,
          " previsão ruim?", previsao_ruim)
    if aviso != "":
        print("  ", aviso)
    decisao = decidir_energia(bateria, consumo, previsao_ruim)
    print("  decisão:", decisao)
    print("  uso de energia:", analisar_uso(geracao, consumo, bateria))

    if decisao == MSG_CRITICO:
        mantidos, desligados = modo_economia(colonia)
        print("  modo economia: mantidos", mantidos, " desligados", desligados)
    print()


def main():
    mostrar_exemplos_do_enunciado()

    colonia = criar_colonia()
    avaliar_colonia("dia normal", colonia, 11)

    colonia = criar_colonia()
    colonia["energetico"]["baterias"]["carga"] = 40
    avaliar_colonia("bateria baixa", colonia, 11)

    colonia = criar_colonia()
    colonia["energetico"]["baterias"]["carga"] = 40
    colonia["operacional"]["laboratorio"]["consumo"] = 30
    avaliar_colonia("crise: bateria baixa, vento fraco e laboratório em pico",
                    colonia, 8)

    colonia = criar_colonia()
    avaliar_colonia("vento fora da faixa", colonia, 30)


main()
