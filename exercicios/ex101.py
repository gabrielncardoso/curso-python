def voto(ano):
    from datetime import date
    atual = date.today().year
    i = atual - ano
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos: VOTO OPCIONAL.'
    elif i >= 18:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'


# PROGRAMA PRINCIPAL
print('-' * 40)
a = int(input('Em que ano você nasceu? '))
print(voto(a))
