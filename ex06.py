DENTRO = []
FORA = []
print("Digite 10 números para verificação: ")
for i in range(0,10):
    num = float(input(f"número {i+1}: "))
    if num>=10 and num<=20:
        DENTRO.append(num)
    else:
        FORA.append(num)
print(f"{len(DENTRO)} estão entre [10,20], {len(FORA)} não estão.")