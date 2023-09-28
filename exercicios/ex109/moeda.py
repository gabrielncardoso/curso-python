def metade(p=0, form=False):
    """
    -> Reduz um preço (p) pela metade.
    :param p: preço
    :param form: Parâmetro opcional. Informa se o preço será ou não formatado pela função moeda().
    :return: a metade do preço inserido.
    """
    res = p / 2
    if form:
        return moeda(res)
    else:
        return res


def dobro(p=0, form=False):
    """
    -> Dobra um preço (p).
    :param p: preço
    :param form: Parâmetro opcional. Informa se o preço será ou não formatado pela função moeda().
    :return: o dobro do preço inserido.
    """
    res = p * 2
    if form:
        return moeda(res)
    else:
        return res


def aumento(p=0, taxa=0, form=False):
    """
    -> Aumenta um preço (p) pelo percentual (taxa) informado.
    :param p: o preço
    :param taxa: o percentual a acrescentar.
    :param form: Indica se o preço retornado será ou não formatado pela função moeda()
    :return: O preço acrescido da taxa
    """
    res = p + (p * taxa / 100)
    if form:
        return moeda(res)
    else:
        return res


def diminuir(p=0, taxa=0, form=False):
    """
    -> Reduz um preço (p) pelo percentual (taxa) informado.
    :param p: o preço
    :param taxa: o percentual a reduzir.
    :param form: Indica se o preço retornado será ou não formatado pela função moeda()
    :return: O preço com a redução da taxa
    """
    res = p - (p * taxa/100)
    if form:
        return moeda(res)
    else:
        return res


def moeda(p=0, moeda='R$'):
    """
    -> Formata um preço (p) no padrão da moeda solicitada.
    :param p: o preço
    :param moeda: o padrão de moeda a formatar (R$, USD, EUR, outros)
    :return: o preço formatado
    """
    return f'{moeda}{p:.2f}'.replace('.', ',')
