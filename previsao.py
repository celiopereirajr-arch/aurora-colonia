# previsao.py
# Desenvolvido com apoio da ferramenta de IA Claude (ver declaração no README).
# Modelo de previsão da colônia: regressão linear simples feita à mão
# (método dos mínimos quadrados, como no capítulo 7).
# Aqui só há contas de previsão. Nenhuma decisão é tomada.


def media(valores):
    """Média: soma dos valores dividida pela quantidade."""
    return sum(valores) / len(valores)


def ajustar_reta(x, y):
    """Encontra a reta y = b0 + b1 * x que melhor passa pelos pontos."""
    media_x = media(x)
    media_y = media(y)
    soma_xy = 0
    soma_xx = 0
    for i in range(len(x)):
        soma_xy = soma_xy + (x[i] - media_x) * (y[i] - media_y)
        soma_xx = soma_xx + (x[i] - media_x) ** 2
    b1 = soma_xy / soma_xx
    b0 = media_y - b1 * media_x
    return b0, b1


def prever(b0, b1, valor_x):
    """Usa a reta para estimar o y de um x novo."""
    return b0 + b1 * valor_x


def r_quadrado(x, y, b0, b1):
    """Mede o quanto a reta explica os dados (1 é ajuste perfeito)."""
    media_y = media(y)
    erro = 0
    total = 0
    for i in range(len(x)):
        erro = erro + (y[i] - prever(b0, b1, x[i])) ** 2
        total = total + (y[i] - media_y) ** 2
    return 1 - erro / total


def prever_energia(vento, vento_hist, energia_hist):
    """Estima a energia eólica para um vento e avisa se ele está fora
    da faixa medida, onde a reta pode errar muito."""
    b0, b1 = ajustar_reta(vento_hist, energia_hist)
    previsao = prever(b0, b1, vento)
    aviso = ""
    if vento < min(vento_hist) or vento > max(vento_hist):
        aviso = "AVISO: vento fora da faixa medida, previsão pouco confiável"
    return previsao, aviso


if __name__ == "__main__":
    vento = [8, 10, 12]
    energia = [20, 25, 30]
    b0, b1 = ajustar_reta(vento, energia)
    print("b0 =", b0, " b1 =", b1)
    print("R2 =", r_quadrado(vento, energia, b0, b1))
    print(prever_energia(11, vento, energia))
    print(prever_energia(30, vento, energia))
