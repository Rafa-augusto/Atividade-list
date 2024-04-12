while True:
    x = int(input("Ínsira um número inteiro de 1 a 10: "))
    A = []
    if x>10 or x<1:
        print("número inválido digite novamente")
        continue
    else:
        for i in range(0,10):
            b = x*(i+1)
            A.append(b)
        print(f"A tábuada de {x} é:\n{A}")
        break