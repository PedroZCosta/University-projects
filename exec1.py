'''
Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas informações.
'''
pair_counter = 0
odd_counter = 0
for i in range(1, 11):
    num = int(input(f"Digite o {i}° numero: "))
    if num % 2 == 0:
        pair_counter += 1
    else:
        odd_counter += 1
print(f"Voce tem {pair_counter} numeros pares")
print(f"Voce tem {odd_counter} numeros impares")

