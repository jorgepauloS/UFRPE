entrada = input().split(";")
dicionario = {}
saida = ""
for i in range(len(entrada)):
    entrada[i] = entrada[i].split()
for i in range(len(entrada)):
    for j in range(len(entrada[i])):
        entrada[i][j] = entrada[i][j].split(":")

for i in range(len(entrada)):
    for j in range(0, len(entrada[i]),2):
        if entrada[i][j][0] == 'A':
            if dicionario.get(entrada[i][j+1][0], False):
                dicionario[entrada[i][j+1][0]] = dicionario[entrada[i][j+1][0]]+"+"+entrada[i][j+1][1]
            else:
                dicionario[entrada[i][j+1][0]] = entrada[i][j+1][1]
        if entrada[i][j][0] == 'R':
            del dicionario[entrada[i][j+1][0]]
        if entrada[i][j][0] == 'B':
            temp = dicionario.get(entrada[i][j+1][0],"oxente?")
            saida += temp + ";"
print(saida)
