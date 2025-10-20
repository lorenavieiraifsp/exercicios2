salario_bruto = float(input("Digite o salário bruto:\n "))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas no mês:\n"))

if salario_bruto < 800:
    desconto = 0
elif salario_bruto <= 1600:
    desconto = salario_bruto * 0.08 + salario_bruto * 0.05
else:
    desconto = salario_bruto * 0.15 + salario_bruto * 0.07

adicional = 0
if horas_trabalhadas > 160:
    valor_hora = salario_bruto / 160
    horas_extras = horas_trabalhadas - 160
    adicional = horas_extras * valor_hora * 0.5

salario_liquido = salario_bruto - desconto + adicional

print("\nSalário líquido: R$ %.2f\n" % salario_liquido)