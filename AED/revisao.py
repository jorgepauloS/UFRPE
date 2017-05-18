def funcao (mes,dia, meses):
    numdia = 0
    for i in range(meses):
        numdia+= numdias[mes]
    numdia = numdia - numerodia[dia]
    return numdia//7

numdias = {"JAN":31, "FEV":28, "MAR":31, "ABR":30, "MAI": 31, "JUN": 30, "JUL":31, "AGO":31, "SET":30, "OUT":31,"NOV":30,"DEZ":31}
nomemes = {1:"JAN", 2:"FEV", 3:"MAR", 4:"ABR", 5:"MAI",6:"JUN",7:"JUL",8:"AGO",9:"SET",10:"OUT",11:"NOV",12:"DEZ"}
numerodia = {"DOM":0,"SEG":1,"TER":2,"QUA":3,"QUI":4,"SEX":5,"SAB":6}

entrada = input()
entrada = entrada.split()
i = 0
j = 1
k = 2
saida = ""
while True:
    if (j > (len(entrada))):
        break
    saida += str(funcao(entrada[i], entrada[j] ,int(entrada[k]))) + " "
    i += 3
    j += 3
    k += 3


mes = entrada[0]
dias = 0
for i in range(int(entrada[2])):
    dias += numdias[mes]
dias = dias - numerodia[entrada[1]]

sabado1 = dias//7

print(saida)
