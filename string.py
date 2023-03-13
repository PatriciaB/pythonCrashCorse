"""
Crie um código declarando as seguintes variáveis do tipo string
"""

# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'


print(nome.upper())
print(cidade.upper())

print(nome.lower())
print(cidade.lower())

letra = 'ã'
print(nome.index(letra))
print(cidade.index(letra))

print('nome ', len(nome))
print('cidade ', len(cidade))
print('cpf ', len(cpf))

for i in cpf:
    if i == '.' or i == '-':
        cpf = cpf.replace(i, '')

print(cpf)