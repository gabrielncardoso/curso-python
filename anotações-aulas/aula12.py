nome = str(input('Qual é seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome in 'Ana Claudia Roberta Vitória':
    print('Belo nome feminino!')
elif nome in 'Matheus Rafael Lucas':
    print('Seu nome é bem popular aqui no Brasil!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))
