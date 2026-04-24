from ECor import COR
from EUbica import UBICA

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
        self.cor = COR.SEMCOR
        self.ubica = ubica
        self.bolinhas = 0


    