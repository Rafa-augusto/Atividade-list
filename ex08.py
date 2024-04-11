while True:
    A = [1]
    num = int(input("Insíra um número positivo para verificação: "))
    if num < 0:
        print("número inválido")
        continue
    else:
        if num%2 == 0:
            A.append(2)
        if num%3 == 0:
            A.append(3)
        if num%4 == 0:
            A.append(4)
        if num%5 == 0:
            A.append(5)
        if num%6 == 0:
            A.append(6)
        if num%7 == 0:
            A.append(7)
        if num%8 == 0:
            A.append(8)
        if num%9 == 0:
            A.append(9)
    print(f"{num} é dvisivel pelos sguintes números:\n{A}")
    break