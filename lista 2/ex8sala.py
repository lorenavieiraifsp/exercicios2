A=int(input("Digite o valor de A.\n"))
B=int(input("Digite o valor de B.\n"))
C=int(input("Digite o valor de C.\n"))

if A%6==0 and B%6==0 and C%6==0:
    print(A, B, C)
elif A%6!=0 and B%6==0 and C%6==0:
    print(B, C)
elif A%6==0 and B%6!=0 and C%6==0:
    print(A, C)
elif A%6==0 and B%6==0 and C%6!=0:
    print(A, B)
else:
    print("Nenhum número é divisível por 2 e 3.\n")

