a = int(input("Digite o primeiro número:\n "))
b = int(input("Digite o segundo número:\n "))
c = int(input("Digite o terceiro número:\n "))

numeros = [a, b, c]
numeros.sort()

print("Menor número:\n", numeros[0])
print("Número do meio:\n", numeros[1])
print("Maior número:\n", numeros[2])
