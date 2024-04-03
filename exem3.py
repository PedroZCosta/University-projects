'''
uso de break
'''
'''
Elaborar um programa que soma 10 numeros usando lacos
'''
soma = 0
contador = 0
for i in range(1, 11):
    num = int(input(f"Digite o {i} numero (0 para encerrar): "))
    if num == 0:
        break
    elif num < 0:
        continue
    contador += 1
    soma += num
print(f"A soma dos {i - 1} numeros é {soma}")
