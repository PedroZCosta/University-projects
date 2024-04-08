"""
Exercicio: Python que gera números entre 1000 e 1999 e mostra aqueles que divididos por 11 dão resto 5.
Criador: Pedro Henrique Zakrzevski Costa
Data: 06/04/2024
Versao: 1.0
"""
for n in range(1000, 2000):
    if n % 11 == 5:
        print(n)
        