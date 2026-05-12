from enum import Enum

'''Vamos a aprovechar el enumerado ya que reacciona a un cierta cantidad 
haremos que ese sea su valor del enumerado
ESQUINA: Reacciona con 2 bolas
LATERAL: Reacciona con 3 bolas
MEDIO: Reacciona con 4 bolas

'''
class ELugar(Enum):
    ESQUINA = 2
    LATERAL = 3
    MEDIO = 4
