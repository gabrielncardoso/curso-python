from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['cpts'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - nasc) + 35
print('-=' * 40)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
