mes = int(input("Digite um número de 1 a 12: "))

match mes:
    case 1:
        print("\nJaneiro\n")
    case 2:
        print("\nFevereiro\n")
    case 3:
        print("\nMarço\n")
    case 4:
        print("\nAbril\n")
    case 5:
        print("\nMaio\n")
    case 6:
        print("\nJunho\n")
    case 7:
        print("\nJulho\n")
    case 8:
        print("\nAgosto\n")
    case 9:
        print("\nSetembro\n")
    case 10:
        print("\nOutubro\n")
    case 11:
        print("\nNovembro\n")
    case 12:
        print("\nDezembro\n")
    case _:
        print("\nMês inválido.\n")
