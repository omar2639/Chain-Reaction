from enum import Enum

'''
-1 A cor que está dentro pode ser:
    - Branco
    - Preto
    - Vermelho
    - Verde
    - SemCor (VEM DE DEFEITO)
'''
class ECOR(Enum):
    BRANCO = 1
    PRETO = 2
    VERMELHO = 3
    VERDE = 4
    SEMCOR = 5