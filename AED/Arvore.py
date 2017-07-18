class Noh:
    def __init__(self,idNoh,listaDados):
        self.idNoh = idNoh
        self.listaDados = listaDados
    def Dados(self):
        return self.listaDados

class ArvoreBn:
    def __init__(self, Noh):
        self.fEsquerdo=None
        self.fDireito=None
        self.Linha=1
        self.Noh=Noh
 
    def add(self, Noh):
        if Noh.idNoh>=self.Noh.idNoh:
            self.addmaior(Noh)
        else:
            self.addmenor(Noh)
 
    def addEsquerdo(self,Noh):
        if self.fEsquerdo:
            self.fEsquerdo.add(Noh)
        else:
            self.fEsquerdo=ArvoreBn(Noh)
 
    def addDireito(self,Noh):
        if self.fDireito:
            self.fDireito.add(Noh)
        else:
            self.fDireito=ArvoreBn(Noh)
 
    def busca(self,Noh):
        if Noh.idNoh>self.Noh.idNoh:
            if self.fDireito:
                return self.fDireito.busca(Noh)
            else:
                return None
        elif Noh.idNoh<self.Noh.idNoh:
            if self.fEsquerdo:
                return self.fEsquerdo.busca(Noh)
            else :
                return None
        else:
            return self.Noh
    def maximo(self,Noh):
        return None
    def minimo(self,Noh):
        return None
tempNoh = Noh(5,"Qualquer merda")
testearv = ArvoreBn(tempNoh)
testearv.add(Noh(3,[1,3]))
testearv.add(Noh(6,[1,6]))
NohBusca = Noh(5,[])
print(testearv.busca(NohBusca).Dados())
