from TCelda import TCelda
from ELugar import ELugar

ALTO = 10
ANCHO = 5
class TTabuleiro:
    

    def __init__(self):
        self.tabuleiro = []
        for i in range(ALTO):
            fila = []
            for j in range(ANCHO):
                if (i == 0 and j == 0) or (i == 0 and j == ANCHO-1) or (i == ALTO - 1 and j == 0) or (i == ALTO -1 and j == ANCHO - 1):
                    celda = TCelda(ELugar.ESQUINA)
                elif (i == 0) or (i == ALTO - 1) or (j == ANCHO - 1) or (j == 0):
                    celda = TCelda(ELugar.LATERAL)
                else:
                    celda = TCelda(ELugar.MEDIO) 
                fila.append(celda)
            self.tabuleiro.append(fila)

    def getCeldaDelTabuleiro(self,x: int,y: int)-> 'TCelda':
        return self.tabuleiro[x][y]
    
    '''Verifica si la coordenada que le estamos dando es valida para modificar la celda
    TRUE: La coordenada es Valida
    FALSE: La coordenada es Invalida'''
    def esCoordenadaValida(self,x:int ,y:int ):
        return not(x < 0 or y < 0 or x >= ALTO or y >= ANCHO) 



    def imprimirTabuleiro(self):
        for i in range(ALTO):
            for j in range(ANCHO):
                match self.tabuleiro[i][j].getLugar():
                    case ELugar.ESQUINA:
                        print(f'E',end = '')
                    case ELugar.LATERAL:
                        print(f'<-L->',end='')
                    case ELugar.MEDIO:
                        print(f'<-M->',end='')
            print()

        print()
        print()
        
    def imprimirTabuleiroValores(self):
        for i in range(ALTO):
            for j in range(ANCHO):
                match self.tabuleiro[i][j].getLugar():
                    case ELugar.ESQUINA:
                        print(f'{self.tabuleiro[i][j].getValor()}',end = '')
                    case ELugar.LATERAL:
                        print(f'<-{self.tabuleiro[i][j].getValor()}->',end='')
                    case ELugar.MEDIO:
                        print(f'<-{self.tabuleiro[i][j].getValor()}->',end='')
            print()
        print()
        print()


    '''Aqui lo que intentare hacer es crear la logica para la reaccion en cadena pero sin los colores
       al momento que llegue a su limite lo que tiene que pasar es que tiene que realizar la accion en cadena
        aumentando mas 1 a las celdas adyacentes '''
    def clicarEnUnValor(self,x,y):
        if not self.esCoordenadaValida(x,y): return
        '''Si al momento de aumentar es verdadero que ya exploto aumentamos mas uno a las celdas adyacente
        usando esta misma funcion lo que generara la reaccion en cadena'''
        if self.getCeldaDelTabuleiro(x,y).aumentarValor():
            self.clicarEnUnValor(x,y-1)
            self.clicarEnUnValor(x-1,y)
            self.clicarEnUnValor(x,y+1)
            self.clicarEnUnValor(x+1,y)
        
        
