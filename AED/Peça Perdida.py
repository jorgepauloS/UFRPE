def descobrir(lista, pos):
    if pos < len(lista)-1:
        if lista[pos]+1 < lista[pos+1]:
            return lista[pos]+1
        else:
            return descobrir(lista, pos+1)
    else:
        return lista[0]-1

entrada = input()
entrada = entrada.split( )
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])
entrada.sort()
print(descobrir(entrada,0))
