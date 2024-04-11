lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
A = []
for i in range(0,9):
    x = lista.count(lista[i])
    A.append(x)
y = A.index(max(A))
print(lista[y])