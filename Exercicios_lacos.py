"""
Exercicio: material radioativo perde metade de sua massa a cada 50 segundos
Criador: Pedro Henrique Zakrzevski Costa
Data: 06/04/2024
Versao: 1.0
"""
time_counter = 0
mass = (input("Por favor, digite a massa total do material: "))
subst = ""
for i in mass:
    if i == ",":
        subst += "."
    else:
        subst += i
num = float(subst)
while True:
    try:
        if num >= 0.5:
            num = num / 2
            time_counter += 50
        else:
            break
    except:
        print("Valor invalido.")
print(f"A sua massa final foi de {num: .2f}g em {time_counter} segundos")