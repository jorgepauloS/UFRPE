#posfilho (n*2)+1

class ArvoreBinariaCheia:
    def __init__(self,tamanho,raiz):
        self.tamanho = (tamanho*tamanho)-1
        self.dados = [None]*self.tamanho
        self.dados[0] = raiz


    def pesquisarNoh(self,Noh,pos,altura):
        if pos >= len(self.dados):
                return 0,0
        if Noh == None or pos == None or self.dados[pos] == None:
            return 0,0
        if (Noh.NohId > self.dados[pos].NohId) and (pos*2+1 < len(self.dados)):
            return self.pesquisarNoh(Noh,(pos*2)+2,altura+1)
        elif (Noh.NohId < self.dados[pos].NohId) and (pos*2+1 < len(self.dados)):
            return self.pesquisarNoh(Noh,(pos*2)+1,altura+1)
        elif Noh.NohId == self.dados[pos].NohId:
            return pos, altura
        else:
            return 0, 0
        
    def adicionarNoh(self,pos,Noh):
        if Noh == None or pos == None or self.dados[pos] == None:
            return 0
        if Noh.NohId > self.dados[pos].NohId:
            if self.Pos(pos,Noh) == None:
                return 0
            self.dados[self.Pos(pos,Noh)] = Noh
            return 1
        elif Noh.NohId < self.dados[pos].NohId:
            if self.Pos(pos,Noh) == None:
                return 0
            self.dados[self.Pos(pos,Noh)] = Noh
            return 1
        else:
            return 0
    def Pos(self,pos,Noh):
        if pos > len(self.dados):
            return 0
        if self.dados[pos] == None:
            return pos
        else:
            if self.dados[pos].NohId > Noh.NohId:
                return self.Pos((pos*2)+1,Noh)
            elif self.dados[pos].NohId < Noh.NohId:
                return self.Pos((pos*2)+2,Noh)
            else:
                return pos
        
            
class NohArvore:
    def __init__(self,NohId,lista):
        self.NohId = int(NohId)
        self.lista = lista       
        

saida = ""
entrada = input().split("!!!")
for i in range(len(entrada)):
    entrada[i] = entrada[i].split()
NovaArvore = ArvoreBinariaCheia(int(entrada[0][0]),NohArvore(entrada[1][0],entrada[1][1]))
entrada = entrada[2:]
for i in range(len(entrada)):
    if len(entrada[i])>1:
        temp = entrada[i][1:]
        temp[0] = temp[0][2:]
        temp[-1] = temp[-1][:-1]
        Noh = NohArvore(entrada[i][0],[temp])
        NovaArvore.adicionarNoh(0,Noh)
    else:
        Noh = NohArvore(entrada[i][0],[])
        temp, altura = NovaArvore.pesquisarNoh(Noh,0,1)
        if altura == 0:
            saida += "0" + "!!!"
        else:
            saida += str(altura) + " " + str(temp) + "!!!"
saida = saida[:-3]
print(saida)
