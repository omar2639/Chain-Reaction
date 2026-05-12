from ELugar import ELugar


class TCelda():
    def __init__(self,lugar: ELugar):
        self.valor = 0
        self.lugar = lugar
        
    def getValor(self):
        return self.valor

    def setValor(self,valor):
        self.valor = valor

    def getLugar(self):
        return self.lugar
    
    '''Esta funcion se va a encargar de decirnos si ya tiene que explotar,
       reduciendo el valor a 0 si ya llego a su limite, retornando:
       TRUE: Si ya exploto la celda
       FALSE: Si aun no exploto '''
    def aumentarValor(self):
        self.valor += 1
        match self.getLugar():
            case ELugar.ESQUINA:
                if self.getValor() == 2:
                    self.setValor(0)
                    return True
            case ELugar.LATERAL:
                if self.getValor() == 3:
                    self.setValor(0)
                    return True
            case ELugar.MEDIO:
                if self.getValor() == 4:
                    self.setValor(0)
                    return True
            
        return False


        