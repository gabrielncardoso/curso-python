print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
total = menorpreço = totmil = 0
nomemaisbarato = ''
cont = 0 #contador para o primeiro preço ser o menor
while True:
    nome = str(input('Nome do Produto: ')).capitalize().strip()
    preço = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preço < menorpreço: #NOME E VALOR DO PRODUTO MAIS BARATO
        nomemaisbarato = nome
        menorpreço = preço
    total += preço #VALOR TOTAL
    if preço > 1000: #PRODUTOS MENOS DE 1000 REAIS
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${menorpreço:.2f}')
