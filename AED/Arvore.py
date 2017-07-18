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
            if temp2.fDireito:
                return temp2.fDireito.Noh.getId()
            else:
                return None
        elif self.ehDireito(nNoh):
            if temp2.fEsquerdo:
                return temp2.fEsquerdo.Noh.getId()
            else:
                return None
        else:
            return None
        
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
            return temp.fEsquerdo
        else:
            return None
        
    def getDireito(self,Noh):
        temp = self.busca(Noh)
        if temp.fDireito:
            return temp.fDireito
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
            else:
                return None
        else:
            return self

    def maximo(self,nNoh):
        temp = self.busca(nNoh)
        if temp == None:
            return None
        while temp.getDireito(temp.Noh):
            temp = temp.getDireito(temp.Noh)
        return temp.Noh
    
    def minimo(self,nNoh):
        temp = self.busca(nNoh)
        if temp == None:
            return None
        while temp.getEsquerdo(temp.Noh):
            temp = temp.getEsquerdo(temp.Noh)
        return temp.Noh
    
    def sucessor(self,nNoh):
        temp = self.busca(nNoh).getDireito(nNoh)
        if temp:
            return self.minimo(temp.Noh).Dados()
        else:
            None
            
    def antecessor(self,nNoh):
        temp = self.busca(nNoh).getEsquerdo(nNoh)
        if temp:
            return self.maximo(temp.Noh).Dados()
        else:
            None
    def verificar(self):
        return None
    def deletar(self,nNoh):
        return None

testearv = ArvoreBn(Noh(14,[14]),None)
lista = [15,4,9,7,18,3,5,16,4,20,17,9,14,5]
for i in lista:
    testearv.add(Noh(i,[i]))
NohBusca = Noh(18,[])
print(testearv.antecessor(NohBusca))

