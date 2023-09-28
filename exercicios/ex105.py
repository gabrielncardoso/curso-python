def notas(*n, sit=False):

    """
    -> Função para analisar notas e situações de alunos de uma turma.
    :param n: uma ou mais notas de um aluno (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com informação de total de notas, maior nota, menor nota, média, e situação da turma.
    """

    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n)/len(n)
    if sit:
        if aluno['média'] < 5:
            aluno['situação'] = 'RUIM'
        if 5 <= aluno['média'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
    return aluno


# PROGRAMA PRINCIPAL
resp = notas(10, 9, 5, 2, 7, 0, sit=True)
print(resp)
