A=float(input("Digite o valor de A.\n"))
B=float(input("Digite o valor de B.\n"))
C=float(input("Digite o valor de C.\n"))

delta= (B*B) - (4 * A * C)

x1= (-B + (delta**0.5))/2
x2= (-B - (delta**0.5))/2

if delta > 0:
    print("As duas raízes são: %.2f %.2f", x1, x2)
else:
    print("Não foi possível calcular")    
