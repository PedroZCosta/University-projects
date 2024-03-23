#informacoes do usuario
salary = float(input("Por favor, digite o seu rendimento mensal em R$: "))
dependentes = int(input("Voce tem dependentes quantos dependentes? "))
pensao = float(input("Por favor, digite quanto voce paga de pensao alimenticia em R$: "))
others = float(input("Por favor, digite outras deducoes: "))
calc_base = salary - (dependentes * 189.59 + pensao + others)
print(f"A sua base de cálculo em R$ e{calc_base: .2f}")

#aliquotas fixas
aliquota2 = 0.075
aliquota3 = 0.150
aliquota4 = 0.225
aliquota5 = 0.275

#calculo final para descobrir IR
if calc_base > 4664.68:
    faixa5 = (calc_base - 4664.68) * aliquota5 + 413.43
    final_payment = salary - faixa5
    print(f"Voce pagou de imposto de renda: R${faixa5: .2f} e seu salario final foi de R${final_payment: .2f}")
elif calc_base > 3751.05 and calc_base < 4664.68:
    faixa4 = (calc_base - 3751.05) * aliquota4 + 207.86
    final_payment = salary - faixa4
    print(f"Voce pagou de imposto de renda: R${faixa4: .2f} e seu salario final foi de R${final_payment: .2f}")
elif calc_base > 2826.65 and calc_base < 3751.05:
    faixa3 = (calc_base - 2826.65) * aliquota3 + 69.2
    final_payment = salary - faixa3
    print(f"Voce pagou de imposto de renda: R${faixa3: .2f} e seu salario final foi de R${final_payment: .2f}")
elif calc_base > 1903.98 and calc_base < 2826.65:
    faixa2 = (calc_base - 1903.98) * aliquota2
    final_payment = salary - faixa2
    print(f"Voce pagou de imposto de renda: R${faixa2: .2f} e seu salario final foi de R${final_payment: .2f}")
else:
    print(f"Voce pagou de imposto de renda: R$0 e seu salario final foi de R${salary: .2f}")