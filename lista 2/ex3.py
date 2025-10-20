nota = float(input("Digite a nota:\n "))
resto = nota - int(nota)

if resto > 0.5:
    nota_arredondada = int(nota) + 1
else:
    nota_arredondada = int(nota)

print("Nota arredondada:\n", nota_arredondada)
