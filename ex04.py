cont = 1
A = []
while True:
    x = int(input("ìnsira o número de idades para a média: "))
    if x<=0:
        print("número inválido")
        continue
    else:
        while cont <= x:
            y = float(input(f"digite a idade da pessoa {cont}: "))
            if y<=0:
                print("idade inválida")
                continue
            else:
                A.append(y)
                cont+=1
        b = (sum(A))/(x)
        print(f"A média de idade destas pessoas é {b:.1f}")
        break