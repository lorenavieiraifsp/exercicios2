primeiranota=float(input("Entre com a primeira nota:\n"))
segundanota=float(input("Entre com a segunda nota:\n"))

media= (primeiranota + segundanota)/2

if media > 6:
    print("Aprovado. sua media eh:%.2f\n" %media)
else:
    print("Reprovado. %.2f\n" %media)

   