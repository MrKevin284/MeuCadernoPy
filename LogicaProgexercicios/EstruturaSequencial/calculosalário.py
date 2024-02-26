# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido. ""


GanhoHora = float(input('Quanto você ganha por hora? '))
HorasTrabalhadasMes = float(input('Quantas horas você trabalha por mês? '))

GanhoTotal = GanhoHora * HorasTrabalhadasMes
print(f"Seu salário total é R${format(GanhoTotal, '.2f')}")

IR = 0.11 * GanhoTotal 
INSS = 0.08 * GanhoTotal
Sindicato = 0.05 * GanhoTotal
SalarioLiquido = GanhoTotal - IR - INSS - Sindicato

print(f'IR (11%): R${format(IR, ".2f")}')
print(f'INSS (8%): R${format(INSS, ".2f")}')
print(f'Sindicato (5%): R${format(Sindicato, ".2f")}')
print(f'Salário Líquido: R${format(SalarioLiquido, ".2f")}')