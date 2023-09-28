from PythonExercicios.ex115.lib.interface import *
from PythonExercicios.ex115.lib.dados import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCriar(nome):
    try:
        a = open(nome, 'wt+')
        print(f'Arquivo {nome} criado com sucesso!')
    except:
        print('ERRO! Não foi possível criar o arquivo!')


def arquivoLer(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! Não foi possível ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]:<30}{dado[1]:>3} anos'.replace('\n', ''))
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{vermelho()}Ocorreu um erro no seu cadastro. Tente novamente!{semcor()}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{vermelho()} Houve um erro na hora de escrever os dados!{semcor()}')
        else:
            print(f'{verde()}Novo registro de {nome} adicionado com sucesso!{semcor()}')