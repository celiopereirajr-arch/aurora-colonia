# decisoes.py
# Regras de decisão da colônia. Recebe números, devolve uma decisão clara.
# Aqui não há dados guardados nem contas de previsão.

# Limites das regras (mudar aqui muda o comportamento do sistema)
ENERGIA_MIN = 50    # bateria abaixo disso é energia baixa
CONSUMO_ALTO = 50   # consumo acima disso é consumo alto

# Texto da decisão mais grave (o main.py usa para acionar o modo economia)
MSG_CRITICO = "CRÍTICO: ativar modo emergência"


def decidir_energia(energia, consumo, previsao_ruim=False):
    """Escolhe a ação segundo a bateria, o consumo e a previsão.
    Ordem das regras: da mais grave para a menos grave."""
    energia_baixa = energia < ENERGIA_MIN
    consumo_alto = consumo > CONSUMO_ALTO

    if energia_baixa and consumo_alto and previsao_ruim:
        return MSG_CRITICO
    elif energia_baixa and consumo_alto:
        return "ALERTA: reduzir consumo"
    elif energia_baixa:
        return "ATENÇÃO: energia baixa"
    else:
        return "OK: sistemas normais"


def analisar_uso(geracao, consumo, reserva=None):
    """Compara geração e consumo e sugere uma ação."""
    if consumo > geracao:
        mensagem = "ALERTA: consumo maior que geração"
        if reserva is not None:
            falta = consumo - geracao
            if reserva >= falta:
                mensagem = mensagem + " (a reserva cobre a diferença)"
            else:
                mensagem = mensagem + " (a reserva não cobre a diferença)"
        return mensagem
    elif geracao > consumo:
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "OK: geração e consumo equilibrados"


def modo_economia(colonia):
    """Mantém os módulos essenciais ligados e desliga os outros."""
    mantidos = []
    desligados = []
    for nome in colonia["operacional"]:
        if colonia["operacional"][nome]["essencial"]:
            mantidos.append(nome)
        else:
            desligados.append(nome)
    return mantidos, desligados


if __name__ == "__main__":
    print(decidir_energia(40, 70))
    print(decidir_energia(40, 70, True))
    print(decidir_energia(40, 30))
    print(decidir_energia(80, 30))
    print(analisar_uso(40, 70))
    print(analisar_uso(80, 30))
    print(analisar_uso(50, 50))
    print(analisar_uso(40, 70, reserva=60))
    print(decidir_energia(50, 70), decidir_energia(49, 50))
