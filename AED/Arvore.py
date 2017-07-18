class Noh:
    def __init__(self,idNoh,listaDados):
        self.idNoh = idNoh
        self.listaDados = listaDados
    def Dados(self):
        return self.listaDados
    def getId(self):
        return self.idNoh

class ArvoreBn:
    def __init__(self, nNoh, nPai):
        self.Pai=nPai
        self.fEsquerdo=None
        self.fDireito=None
        self.Noh=nNoh

    def getIrmao(self,nNoh):
        temp = self.getPai(nNoh)
        if temp == None:
            return None
        temp2 = self.busca(Noh(temp,None))
        if self.ehEsquerdo(nNoh):
            return temp2.fDireito.Noh.getId()
        elif self.ehDireito(nNoh):
            return temp2.fEsquerdo.Noh.getId()
    def ehEsquerdo(self,nNoh):
        temp = self.getPai(nNoh)
        if temp == None:
            return False
        temp2 = self.busca(Noh(temp,None))
        temp3 = None
        if temp2.fEsquerdo:
            temp3 = temp2.fEsquerdo.Noh.getId()
        if temp3 == nNoh.getId():
            return True
        else:
            return False
    def ehDireito(self,nNoh):
        temp = self.getPai(nNoh)
        if temp == None:
            return False
        temp2 = self.busca(Noh(temp,None))
        temp3 = None
        if temp2.fDireito:
            temp3 = temp2.fDireito.Noh.getId()
        if temp3 == nNoh.getId():
            return True
        else:
            return False
    
    def getInfo(self,Noh):
        return self.busca(Noh).Noh.Dados()
    def getPai(self,Noh):
        temp = self.busca(Noh)
        if temp.Pai:
            return temp.Pai.Noh.getId()
        else:
            return None
    def getEsquerdo(self,Noh):
        temp = self.busca(Noh)
        if temp.fEsquerdo:
            return temp.fEsquerdo.Noh
        else:
            return None
    def getDireito(self,Noh):
        temp = self.busca(Noh)
        if temp.fDireito:
            return temp.fDireito.Noh
        else:
            return None
    def add(self, Noh):
        if Noh.idNoh>=self.Noh.idNoh:
            self.addDireito(Noh)
        else:
            self.addEsquerdo(Noh)
 
    def addEsquerdo(self,Noh):
        if self.fEsquerdo:
            self.fEsquerdo.add(Noh)
        else:
            self.fEsquerdo=ArvoreBn(Noh,self)
 
    def addDireito(self,Noh):
        if self.fDireito:
            self.fDireito.add(Noh)
        else:
            self.fDireito=ArvoreBn(Noh,self)
 
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
            return self
        
    def maximo(self):
        Noh = self.Noh
        while self.getDireito(Noh):
            Noh = self.getDireito(Noh)
        return Noh
    def minimo(self):
        Noh = self.Noh
        while self.getEsquerdo(Noh):
            Noh = self.getEsquerdo(Noh)
        return Noh
    
tempNoh = Noh(5,"Qualquer merda")
testearv = ArvoreBn(tempNoh,None)
testearv.add(Noh(2,[1,2]))
testearv.add(Noh(3,[1,3]))
testearv.add(Noh(1,[1,1]))
testearv.add(Noh(7,[1,7]))
testearv.add(Noh(6,[1,6]))
testearv.add(Noh(8,[1,8]))
NohBusca = Noh(8,[])
print(testearv.getIrmao(NohBusca))
