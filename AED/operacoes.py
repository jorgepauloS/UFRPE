entrada = input().split()
teste = 0
multi = []
op = []
for i in range(len(entrada)):
    nova = 0
    if entrada[i] == 'LOOP':
        multi.append(int(entrada[i+1]))
    elif entrada[i] == 'OP':
        op.append(int(entrada[i+1]))
    elif entrada[i] == 'INICIO':
        multi.append(1)
for i in range(10):
    teste += multi[i]*op[i]
print(teste)

