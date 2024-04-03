"""
Exercicio: Cáculo do Imposto de Renda - IRPF
Criador: Pedro Henrique Zakrzevski Costa
Data: 28/03/2024
versao: 1.3
"""
# porcentagens aliquotas fixas do IRPF
aliquota2 = 0.075
aliquota3 = 0.150
aliquota4 = 0.225
aliquota5 = 0.275
# faixas do IRPF
fax1 = 1903.98
fax2 = 2826.65
fax3 = 3751.05
fax4 = 4664.68
# Valor da dedução por dependente
dep = 189.59
# informacoes do usuario
salary = float(input("Por favor, digite o salario bruto em R$: "))
dependentes = int(input("Por favor, digite o número de dependetes (0 para nenhum): "))
pensao = float(input("Por favor, digite o valor de pensão (0 para nenhum): "))
others = float(input("Por favor, digite o valor de outras deduções (0 para nenhum): "))
# Calculo da base de calculo
calc_base = salary - (dependentes * dep + pensao + others)
print(f"A sua base de cálculo e R${calc_base: .2f}")
# calculo final para descobrir IR
fc2 = (fax2 - fax1) * aliquota2
fc3 = (fax3 - fax2) * aliquota3 + fc2
fc4 = (fax4 - fax3) * aliquota4 + fc3
if calc_base <= fax1:
    final_salary = salary
    final_p = 0
    f = "1"
elif calc_base >= fax1:
    ir2 = (calc_base - fax1) * aliquota2
    final_p = ir2
    final_salary = salary - ir2
    f = "2"
elif calc_base >= fax2:
    ir3 = (calc_base - fax2) * aliquota3 + fc2
    final_p = ir3
    final_salary = salary - ir3
    f = "3"
elif calc_base >= fax3:
    ir4 = (calc_base - fax3) * aliquota4 + fc3
    final_p = ir4
    final_salary = salary - ir4
    f = "4"
else:
    ir5 = (calc_base - fax4) * aliquota5 + fc4
    final_p = ir5
    final_salary = salary - ir5
    f = "5"
# Calcular a alíquota efetiva do IRPF
aliquota_efet = final_p / calc_base * 100
print(f"Voce se encaixa na faixa {f} e ira pagar R${final_p: .2f} e seu salario final foi de R${final_salary:.2f}")
print(f"A alíquota efetiva do seu imposto de renda é {aliquota_efet: .1f}%")

