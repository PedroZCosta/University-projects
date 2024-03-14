#Exercício 2: Calculadora de IMC (Índice de Massa Corporal)
peso = float(input("Qual seu peso? "))
alt = float(input("Qual sua altura? (Exemplo : 1.83) "))
imc = int(peso / (alt **2))
print ("Seu resultado e:", imc)
if imc <= 16.9:
    print("Voce esta muito abaixo do peso!")
elif (imc >= 17) and (imc <= 18.9):
    [print ("Voce esta abaixo do peso!")]
elif (imc >= 18.5) and (imc <= 24.9):
    [print ("Voce tem um peso normal!")]
elif (imc >= 25) and (imc <= 29.9):
    [print ("Voce esta acima do peso!")]
elif (imc >= 30) and (imc <= 34.9):
    [print("Voce tem obesidade grau 1!")]
elif (imc >= 35) and (imc <= 40):
    [print ("Voce tem obesidade grau 2!")]
else:
    print ("Voce tem obesidade grau 3!")