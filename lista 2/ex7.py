codigo = int(input("Digite o código do curso (1 a 5): "))

match codigo:
    case 1:
        print("\nEngenharia\n")
    case 2:
        print("\nEdificações\n")
    case 3:
        print("\nSistemas Elétricos\n")
    case 4:
        print("\nTurismo\n")
    case 5:
        print("\nAnálise de Sistemas\n")
    case _:
        print("\nCódigo inválido.\n")
