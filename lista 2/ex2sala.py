A=float(input("Entre com a primeira nota:\n"))
B=float(input("Entre com a segunda nota:\n"))

media= (A+B)/2

if media >= 6:
    print("Aprovado\n")
else:
    exame=float(input("Entre com a nota do exame:\n"))
novamedia= (A+B+exame)/3
if novamedia >= 6:
    print("Aprovado com media:", novamedia)
else:
    print("Reprovado com media:\n", novamedia)    