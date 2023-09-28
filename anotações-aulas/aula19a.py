estado = {}
brasil = []
for c in range(0, 2):
    estado['uf'] = str(input('Nome do Estado: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
        print(f'O estado {e["uf"]} tem a sigla {e["sigla"]}')
