cores = {'ciano':'\033[36m',
         'limpa':'\033[m'}
nome = input('Digite o seu nome: ')
print('É um prazer te conhecer, {}{}{}!' .format(cores['ciano'], nome, cores['limpa']))
