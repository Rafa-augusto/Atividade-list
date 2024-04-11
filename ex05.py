PARES = []
IMPARES = []
print("Escolha 10 números para verificar se são pares ou ímpares: ")
for i in range(0,10):
    num = float(input(f"número {i+1}: "))
    if num%2 != 0:
        IMPARES.append(num)
    else:
        PARES.append(num)
print(f"{len(PARES)} são pares, {len(IMPARES)} são ímpares.")