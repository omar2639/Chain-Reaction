'''
    Agora esse de aqui faz o seguiente recebe onde foi clickado e realiza a ação correspondente
    Para o nosso projeto, vamos implementar uma IA baseada em Aprendizado por Reforço.
    A ideia é que a IA aprenda sozinha quais jogadas são melhores através de um sistema de recompensas
    e punições.
    0. Interface de Comunicação
    A classe TJogadorIA deve ser desacoplada da interface gráfica. 
    Ela funciona assim:
    Entrada: Recebe o estado atual da matriz (tabuleiro).
    Saída: Retorna uma tupla (x, y) com a coordenada onde deseja jogar.
    Feedback: Recebe da TLogicaFinal um valor numérico (Recompensa) e uma String de Status.
    1. Tabela de Recompensas: Quando você pesquise sobre o aprendizado por reforço vai cair em conta
     de que a IA aprende segundo seus erros então ao momento de mostrar o jogo para a professora temos
      que fazer que a IA passe de uma "clicadora aleatória" para uma "mestra do jogo", 
      você deve seguir rigorosamente estes valores de recompensa:
      Situação              Recompensa                  Código de Status (para o Offset)
      Fora dos limites      -20                         "ERR_OUT"
      Célula Inimiga        -5                          "ERR_INVALID"
      Vitória (Final)       +100                        "WINNER"
      Derrota (Final)       -100                        "GAME_OVER"
      Jogada em Esquina     +2                          "SUCCESS_CORNER"
      Reação em Cadeia      +2 * (celulas_capturadas)   "CHAIN_REACTION"
      Jogada Válida Comum   0                           "SUCCESS"


    Agora sua missão é a mais importante porque você vai se encarregar de pesquisar como funciona a IA
    e em que momento a gente tem que fazer tudo lembra, você pode anhadir funcões, por acaso, não sei
    quase nada de IA então o template foi feito por uma, agora se estiver errado, fala

    
'''

class TJogadorIA:
    def __init__(self, cor_ia):
        self.cor = cor_ia
        self.memoria = {} # Q-Table: guarda o valor de cada (estado, acao)
        self.taxa_aprendizado = 0.1

    def decidir_jogada(self, matriz):
        # Analisa a matriz e escolhe (x, y)
        # No início, use escolhas aleatórias (exploração)
        #return (x, y)
        pass

    def aprender(self, estado_anterior, acao, recompensa, estado_novo):
        # Aqui a mágica acontece. 
        # Se a recompensa foi +100, ela reforça que essa jogada é excelente.
        # Se foi -20, ela aprende a nunca mais clicar ali naquele estado.
        pass