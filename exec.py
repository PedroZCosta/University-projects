"""
Exercicio: IMC – Índice de Massa Corporal
Criador: Pedro Henrique Zakrzevski Costa
Data: 29/03/2024
versao: 1.4
"""
# Faixas do IMC
range1 = 16.5
range2 = 24.9
range3 = 29.9
range4 = 34.9
range5 = 39.9
# Solicita as informacoes do usuario
peso = float(input("Digite seu peso? "))
alt = float(input("Digite sua altura em metros (exemplo : 1.83): "))
imc = (peso / (alt ** 2))
print(f"Seu resultado é:{imc: .1f}")
# Encontra onde o usuario se encontra na tabela do IMC
if imc < range1:
    print("Voce esta abaixo do peso!")
elif (imc >= range1) and (imc < range2):
    print("Voce tem um peso normal!")
elif (imc >= range2) and (imc < range3):
    print("Voce esta acima do peso!")
elif (imc >= range3) and (imc < range4):
    print("Voce tem obesidade grau 1!")
elif imc >= range4 and (imc < range5):
    print("Voce tem obesidade grau 2!")
else:
    print("Voce tem obesidade grau 3!")
