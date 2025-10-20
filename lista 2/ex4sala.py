A=int(input("Entre com o valor de A:\n"))
B=int(input("Entre com o valor de B:\n"))
C=int(input("Entre com o valor de C:\n"))

if A<B+C and B<A+C and C<A+B:
    print("É um triângulo.\n")
    if A==B or B==C or C==A:
     print("O seu triângulo é isóceles.\n") 
    elif A!=B and B!=C:
     print("O seu triângulo é escaleno.\n")
    else:
     print("É equilátero.\n")
else:
   print("Não é um triângulo.\n")
