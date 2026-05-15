from JuegoPrincipal.ECor import ECOR
from JuegoPrincipal.EUbica import EUBICA

'''
A classe que a gente está criando aquí vai nos permitir saber
-1 A cor que está dentro pode ser:
    - Branco
    - Preto
    - Vermelho
    - Verde
    - SemCor (VEM DE DEFEITO)
-2 A quantia de bolinhas que tem, a gente não vai se importar
 muito com a cor nesse caso porque pode mudar em qualquer momento
-3 Onde é que fica a Celula no Tabuleiro por o motivo de que:
    -Quina: Vai reagir quando tiver 2 bolinhas
    -Lateral: Vai reagir quando tiver 3 bolinhas
    -Corpo: Vai reagir quanto tiver 4 bolinhas

'''
class TCelula:

    def __init__(self, ubica):
        self.cor = ECOR.SEMCOR
        self.ubica = ubica
        self.bolinhas = 0


    def getBolinhas(self):
        return self.bolinhas
    
    def setBolinhas(self,bolinhas: int):
        self.bolinhas = bolinhas

    def getCor(self)-> ECOR:
        return self.cor
    
    def setCor(self, cor: ECOR):
        self.cor = cor

    def getUbicacao(self) -> EUBICA:
        return self.ubica
    
    '''Essa funcao vai dizer se a gente chegou ao limite
    de bolinhas possiveis do lugar onde esta, se for assim
    tornamos o valor a 0 e retornamos TRUE e se nao FALSE''' 
    def aumentarUmaBolinha(self,cor: ECOR):
        self.bolinhas += 1
        self.setCor(cor=cor)
        match self.getUbicacao():
            case EUBICA.QUINA:
                if self.getBolinhas() == 2:
                    self.setBolinhas(0)
                    return True
            case EUBICA.LATERAL:
                if self.getBolinhas() == 3:
                    self.setBolinhas(0)
                    return True
            case EUBICA.CORPO:
                if self.getBolinhas() == 4:
                    self.setBolinhas(0)
                    return True
            
        return False