from PythonExercicios.ex115.lib.interface import *  # ASTERISCO NO FINAL IMPORTA TUDO
from PythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
else:
    arquivoCriar(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo.
        arquivoLer(arq)
        sleep(2)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('Cadastrar nova pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif resp == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema...')
        sleep(1)
        break
    else:
       print(f"{vermelho()}ERRO! Digite uma opção válida!{semcor()}")
       sleep(1)
