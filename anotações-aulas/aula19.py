pessoas = {'nome': 'Gabriel', 'idade': 25, 'sexo': 'Masculino'}
pessoa2 = {'nome': 'Ana Vitória', 'idade': 30, 'sexo': 'Feminino'}
lista = [pessoas, pessoa2]
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"].lower()}!')
print(lista[1]['idade'])
pessoas['nome'] = 'Lucas'
pessoas['peso'] = 85
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')