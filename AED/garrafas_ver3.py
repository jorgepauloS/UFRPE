def tomar(cheias, emprestado):
    vazias = 0
    vazias += cheias
    vazias += emprestado
    tomadas = cheias
    if vazias > 3:
        cheias = (vazias//3)
        vazias = (vazias%3)
        var1, var2 = tomar(cheias,vazias)
        tomadas += var1
        return tomadas, vazias
    elif vazias ==3:
        cheias = (vazias//3)
        vazias = (vazias%3)
        var1, var2 = tomar(cheias,vazias)
        tomadas += var1
        return tomadas, vazias
    else:
        tomadas += vazias
        return tomadas, vazias

entrada = input().split()
verif = 0
saida = ""
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

for i in range(len(entrada)):
    if ((entrada[i]%3)==0):
        total, vazio = tomar(entrada[i], 0)
        total = total-1
        saida += str(total) + " "
    elif ((entrada[i]%3)==1):
        verif = 1
        total, teste = tomar(entrada[i], verif)
        total = total-2
        saida += str(total) + " "
    else:
        verif = 2
        total, teste = tomar(entrada[i], verif)
        total = total-2
        saida += str(total) + " "
print(saida)
