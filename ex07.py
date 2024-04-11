PARES = []
for i in range(0,101):
    if i%2 == 0:
        PARES.append(i)
print(f"A soma dos 50 primeiros números pares é {sum(PARES)}.")
print(len(PARES))