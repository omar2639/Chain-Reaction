from JuegoPrincipal.TCelula import TCelula
from JuegoPrincipal.EUbica import EUBICA
from JuegoPrincipal.ECor import ECOR

COMPRIMENTO = 10
LARGURA = 5

class TTabuleiro():
    def __init__(self):
        self.tabuleiro = []
        for i in range(COMPRIMENTO):
            fila = []
            for j in range(LARGURA):
                #Aqui temos que definir onde é que fica a celula
                if (i == 0 and j == 0) or (i == 0 and j == LARGURA-1) or (i == COMPRIMENTO - 1 and j == 0) or (i == COMPRIMENTO -1 and j == LARGURA - 1):
                    celula = TCelula(EUBICA.QUINA)
                elif (i == 0) or (i == COMPRIMENTO - 1) or (j == LARGURA - 1) or (j == 0):
                    celula = TCelula(EUBICA.LATERAL)
                else:
                    celula = TCelula(EUBICA.CORPO) 
                fila.append(celula)
            self.tabuleiro.append(fila)


    def getCelulaDoTabuleiro(self,x: int,y: int)-> 'TCelula':
        return self.tabuleiro[x][y]
    
    '''Verifica se a coordena é correta
    TRUE: A coordenada é Valida
    FALSE: A coordenada é Invalida'''
    def eCoordenadaValida(self,x:int ,y:int ):
        return not(x < 0 or y < 0 or x >= COMPRIMENTO or y >= LARGURA) 



    def imprimirTabuleiro(self):
        for i in range(COMPRIMENTO):
            for j in range(LARGURA):
                match self.getCelulaDoTabuleiro(i,j).getUbicacao():
                    case EUBICA.QUINA:
                        print(f'E',end = '')
                    case EUBICA.LATERAL:
                        print(f'<-L->',end='')
                    case EUBICA.CORPO:
                        print(f'<-M->',end='')
            print()

        print()
        print()
        
    def imprimirTabuleiroValores(self):
        for i in range(COMPRIMENTO):
            for j in range(LARGURA):
                match self.getCelulaDoTabuleiro(i,j).getUbicacao():
                    case EUBICA.QUINA:
                        print(f'{self.tabuleiro[i][j].getBolinhas()}',end = '')
                    case EUBICA.LATERAL:
                        print(f'<-{self.tabuleiro[i][j].getBolinhas()}->',end='')
                    case EUBICA.CORPO:
                        print(f'<-{self.tabuleiro[i][j].getBolinhas()}->',end='')
            print()
        print()
        print()


    '''Aqui lo que intentare hacer es crear la logica para la reaccion en cadena pero sin los colores
       al momento que llegue a su limite lo que tiene que pasar es que tiene que realizar la accion en cadena
        aumentando mas 1 a las celdas adyacentes '''
    '''
    Aqui vai acontecer o seguinte se o jogador conseguir chegar aqui da para que aumentar
    as bolinhas da celula, e tambem mudar a cor 
    '''
    def clicarEnUnValor(self,x: int,y: int, cor: ECOR):

        if not self.eCoordenadaValida(x,y): return
        '''Si al momento de aumentar es verdadero que ya exploto aumentamos mas uno a las celdas adyacente
        usando esta misma funcion lo que generara la reaccion en cadena'''
        if self.getCelulaDoTabuleiro(x,y).aumentarUmaBolinha(cor):
            self.clicarEnUnValor(x,y-1,cor)
            self.clicarEnUnValor(x-1,y,cor)
            self.clicarEnUnValor(x,y+1,cor)
            self.clicarEnUnValor(x+1,y,cor)
        

    def printarAsCores(self):   
        for i in range(COMPRIMENTO):
            for j in range(LARGURA):
                match self.getCelulaDoTabuleiro(i,j).getUbicacao():
                    case EUBICA.QUINA:
                        print(f'{str(self.getCelulaDoTabuleiro(i,j).getCor())}',end = '')
                    case EUBICA.LATERAL:
                        print(f'<-{str(self.getCelulaDoTabuleiro(i,j).getCor())}->',end='')
                    case EUBICA.CORPO:
                        print(f'<-{str(self.getCelulaDoTabuleiro(i,j).getCor())}->',end='')
            print()
        print()
        print()