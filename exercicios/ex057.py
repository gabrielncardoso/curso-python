# VALIDAÇÃO DE DADOS - SEXO M OU F
sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
        sexo = str(input('Dados inválidos. Por favor, informe o seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
