'''
Elaborar um programa que soma 10 numeros usando lacos
'''
soma = 0
for i in range(10):
    num = int(input(f"Digite o {i} numero:"))
    soma += num
print(f"A soma dos 10 numeros é {soma}")
