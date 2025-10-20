numero_chave = 20
num = int(input("Digite um número entre 0 e 100:\n"))

if 0 <= num <= 100:
    distancia = abs(numero_chave - num)
    print("Distância do número chave:\n", distancia)
else:
    print("Número fora do intervalo:\n")
