"""
3. Altere o código da atividade 1, criando uma variável divisor e, em seguida,
verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e
excluindo o 1000) são múltiplos da variável divisor
"""

# declaração das variáveis
inicio = 0
fim = 1000
divisor = 3
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
 if numero % divisor == 0:
    print(numero)