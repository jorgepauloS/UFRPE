def magicodiag1(quadrado, tamanho, resultado):
    teste = 0
    for i in range(tamanho):
        teste += quadrado[i][i]
    if teste == resultado:
        return True
    else:
        return False
def magicodiag2(quadrado, tamanho, resultado):
    teste = 0
    for i in range(tamanho):
        if teste == 0:
            teste += quadrado[-1][i]
        else:
            teste += quadrado[-i-1][i]
    if teste == resultado:
        return True
    else:
        return False
    return
def magicolinha(quadrado, tamanho, resultado):
    teste = 0
    for linha in range(tamanho):
        for coluna in range(tamanho):
            teste += quadrado[linha][coluna]
        if teste == resultado:
            teste = 0
        else:
            return False
    return True

entrada = input()
entrada = entrada.split( )
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])
tamanho = entrada[0]
resultado = int((entrada[0]+(entrada[0]*entrada[0]*entrada[0]))/2)
temp = []
quad = []*tamanho
soma = 0


for i in range(tamanho):
    for j in range(tamanho):
        temp.append(entrada[(i*tamanho)+j+1])
    quad.append(temp)
    temp = []
for i in range(tamanho):
    soma += quad[0][i]

diagonalpri = magicodiag1(quad,tamanho,soma)
diagonalsec = magicodiag2(quad,tamanho, soma)
linhas = magicolinha(quad,tamanho, soma)
if (diagonalpri and diagonalsec and linhas):
    print(soma)
else:
    print(-1)      
