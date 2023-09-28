def leiadinheiro(msg):
    valido = False
    while not valido:
        resp = str(input(msg)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\033[0;31mERRO! "{resp}" é um preço inválido!\033[m')
        else:
            valido = True
    return float(resp)
