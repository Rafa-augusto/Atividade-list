import random
while True:
    A = [1]
    num = int(input("Insíra um número positivo para verificação: "))
    if num < 0:
        print("número inválido")
        continue
    else:
       for i in range(0,9999999):
           x = random.randint(1,(num))
           if num%x == 0:
               A.append(x)
    print(f"{num} é dvisivel pelos sguintes números:\n{list(set(A))}")
    break
#possuí seus limites.Não sabia se era para apresentar literalemnte todos os divisores ou não.