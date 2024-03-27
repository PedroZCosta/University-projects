#informacoes do usuario
salary = float(input("Por favor, digite o seu rendimento mensal em R$: "))
dependentes = int(input("Voce tem dependentes quantos dependentes? "))
pensao = float(input("Por favor, digite quanto voce paga de pensao alimenticia em R$: "))
others = float(input("Por favor, digite outras deducoes: "))
calc_base = salary - (dependentes * 189.59 + pensao + others)
print(f"A sua base de cálculo em R$ e{calc_base: .2f}")
#aliquotas fixas e faixas fixas
aliquota2 = 0.075
aliquota3 = 0.150
aliquota4 = 0.225
aliquota5 = 0.275
fax1 = 1903.98
fax2 = 2826.65
fax3 = 3751.05
fax4 = 4664.68
#calculo final para descobrir IR
if calc_base > fax1:
    faixa = (calc_base - fax1) * aliquota2
    final_payment = salary - faixa
elif calc_base > fax2:
    faixa = (calc_base - fax2) * aliquota3 + 69.2
    final_payment = salary - faixa
elif calc_base > fax3:
    faixa = (calc_base - fax3) * aliquota4 + 207.86
    final_payment = salary - faixa
elif calc_base > fax4:
    faixa = (calc_base - fax4) * aliquota5 + 413.43
    final_payment = salary -faixa
else:
    print(f"Voce pagou de imposto de renda: R$0 e seu salario final foi de R${salary: .2f}")

print(f"Voce pagou de imposto de renda: R${faixa: .2f} e seu salario final foi de R${final_payment: .2f}")
