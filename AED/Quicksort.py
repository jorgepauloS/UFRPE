from random import randrange

def quicksort(lista, comeco, fim):
    if comeco < fim:
        qualquer = org(lista, comeco, fim)
        quicksort(lista,qualquer[1],qualquer[0]-1)
        quicksort(lista,qualquer[0]+1,qualquer[2])
def org(lista, comeco, fim):
    indice = lista[fim]
    i = comeco-1
    
    for j in range(comeco,fim):
        if lista[j] <= indice:
            i += 1
            lista[i],lista[j] = lista[j],lista[i]
            
    lista[i+1],lista[fim]=lista[fim],lista[i+1]
    return i+1,comeco,fim


entrada = input()
list(entrada)
x = entrada.split(" ")
saida = ""

for i in range(len(x)):
    x[i] = int(x[i])
    
quicksort(x,0,len(x)-1)

for i in x:
    saida += str(i)+ " "
    
print(saida)


    
