import random 
#===============================================================
#Grupo 35 - Alameda
#Daniel Ramos, n 81620
#Rafael Belchior, n 80979
# Nota: 17,85

#===============================================================
#Funcoes auxiliares para TAD COORDENADAS

def numero_1_a_4(arg):            #Verifica se o argumento e um inteiro de 1 a 4
    return inteiro(arg) and arg>0 and arg<5 and arg is not bool

def inteiro (n):                                #Verifica se um numero e inteiro
    return isinstance(n,int) and not isinstance(n,bool)

def multiplo_4(n):               #Verifica se o numero inteiro n e multiplo de 4
    return inteiro(n) and n%4 == 0
           
#===============================================================
#TAD COORDENADAS


#Construtor
def cria_coordenada(l,c):
    """Corresponde ao construtor do tipo coordenada. Recebe dois argumentos
      do tipo inteiro e devolve um elemento do tipo coordenada correspondente \
      a posicao (linha, coluna)"""    
    
    if numero_1_a_4(l) and numero_1_a_4(c):
        return (l,c)
    else:
        raise ValueError ("cria_coordenada: argumentos invalidos")
    
    
#Seletor
def coordenada_linha(coordenadas):
    """Recebe dois argumentos do tipo inteiro: devolve o primeiro, 
    que corresponde a uma linha l"""
    
    return coordenadas[0]

#Seletor
def coordenada_coluna(coordenadas):
    """Recebe dois argumentos do tipo inteiro: devolve o primeiro, 
    que corresponde a coluna c""" 
    
    return coordenadas[1]


#Reconhecedor
def e_coordenada(coord): 
    """ Recebe um argumento e devolve verdadeiro caso esse argumento
    seja do tipo coordenada, e falso em caso contrario. """
    
    if isinstance(coord,tuple) and len(coord) == 2:
        if numero_1_a_4(coordenada_linha(coord)) and \
           numero_1_a_4(coordenada_coluna(coord)):
            return True
    return False


#Teste
def coordenadas_iguais(c1,c2):
    """Recebe como argumentos dois elementos do tipo coordenada e devolve
    verdadeiro caso esses argumentos correspondam a mesma posicao (l; c) 
    do tabuleiro, e falso em caso contrario."""
    
    return c1 == c2

    
#================================================================
#TAD TABULEIRO

#Construtor
#cria_tabuleiro devolve uma lista cujos elementos sao listas vazias mais um 
# elemento zero correspondente a pontuacao. Cada sublista corresponde a uma 
# linha e cada indice corresponde a uma coluna.
def cria_tabuleiro():
    """devolver um elemento do tipo tabuleiro (vazio)""" 
    
    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0] 

#Seletor
def tabuleiro_posicao(tab,coord):
    """Devolve um elemento do tipo inteiro, que corresponde
    ao valor na posicao do tabuleiro correspondente a coordenada"""
    
    if e_coordenada(coord):
        return tab[coordenada_linha(coord)-1][coordenada_coluna(coord)-1]
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    
#Seletor    
def tabuleiro_pontuacao(tab):
    """Devolve a pontuacao atual para o tabuleiro"""
    
    return tab[4]

#Seletor
def tabuleiro_posicoes_vazias (tab):
    """Devolve uma lista contendo as coordenadas de todas 
    as po vazias do tabuleiro t"""
    
    lista=[]
    for l in range(1,5):                     #para cada linha
        for c in range(1,5):                 #para cada coluna
            if tabuleiro_posicao(tab,cria_coordenada(l,c)) == 0: #se a
                #coordenada de certa posicao for 0
                lista = lista + [cria_coordenada(l,c)]          #adicionar a lista com coordenadas que sao 0       
    return lista


#Modificador
def tabuleiro_preenche_posicao(tab,coord,v):
    """Recebe um elemento do tipo tabuleiro, um elemento do tipo coordenada e um
    inteiro v. Modifica o tabuleiro t, colocando o valor v na posicao da 
    coordenada c"""
    
    if e_coordenada(coord) and inteiro(v) :
        tab[coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1] = v
        return tab
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')
    
    
#Modificador    
def tabuleiro_actualiza_pontuacao(tab,v):
    """Recebe um elemento do tipo tabuleiro e um inteiro v nao negativo multiplo
    de 4. Modifica o tabuleiro, acrescentando o valor da pontuacao v pontos"""
    
    if e_tabuleiro(tab) and multiplo_4(v):
        tab[4]=tab[4] + v   #adiciona a pontuacao (indice 4 da 
                            #representacao interna) v pontos
        return tab
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')



#================================================================     
#Modificador
def tabuleiro_reduz(tab,direcao):
    """Recebe elemento do tipo tabuleiro e cadeia de carateres de correspondente
    a direcao da reducao. Reduz o tabuleiro na direcao d e devolve o tabuleiro
    modificado"""

#A funcao tab_reduz_aux recebe um tabuleiro, direcao e valores 

    def tab_reduz_aux(tab,direcao,i_linha,i_coluna,l,c):
        tab = zeros_entre_coord(tab,direcao,c,l)
        if tabuleiro_posicao(tab,cria_coordenada(l,c)) == \
           tabuleiro_posicao(tab,cria_coordenada(l+i_linha,c+i_coluna)) \
           and tabuleiro_posicao(tab,cria_coordenada(l,c))!=0:
            tab = tabuleiro_preenche_posicao(tab,cria_coordenada(l,c),\
                                             tabuleiro_posicao(tab,cria_coordenada(l,c))*2)  
            tab = tabuleiro_preenche_posicao(tab,cria_coordenada(l+i_linha,c+i_coluna),0)
            tab = tabuleiro_actualiza_pontuacao\
                (tab,tabuleiro_posicao(tab,cria_coordenada(l,c)))
            tab=zeros_entre_coord(tab,direcao,c,l)          
    
    
    if direcao=='E': 
        #Se a direcao for Este, a lista e percorrida e corresponde as colunas
         # da direita para a esquerda
        i_linha = 0
        i_coluna = -1        
        for l in range(1,5):
            for c in range(4,1,-1):
                tab_reduz_aux(tab,direcao,i_linha,i_coluna,l,c)
                
                
    elif direcao=='W':
        #Se a direcao for Oeste, a lista e percorrida e corresponde as colunas
          # da esquerda para a direita 
              
        i_linha = 0
        i_coluna = 1
        for l in range(1,5):
            for c in range(1,4):
                tab_reduz_aux(tab,direcao,i_linha,i_coluna,l,c)
                
                                 
    elif direcao=='N':
        #Se a direcao for Norte, a lista e percorrida  e corresponde as linhas
         # de cima para baixo      

        i_linha = 1
        i_coluna = 0
        for c in range(1,5):
            for l in range(1,4):
                tab_reduz_aux(tab,direcao,i_linha,i_coluna,l,c)
            
            
    elif direcao=='S':
        #Se a direcao for Sul, a lista e percorrida  e corresponde as linhas
         # de baixo para cima          

        i_linha = -1
        i_coluna = 0
        for c in range(1,5):
            for l in range(4,1,-1):
                tab_reduz_aux(tab,direcao,i_linha,i_coluna,l,c)
                   
    else:
        raise ValueError ("tabuleiro_reduz: argumentos invalidos") 
                
    return tab    
    
  

#==========================Funcoes auxiliares de tabuleiro_reduz=======================================

def quais_valores(direcao):
    #Define os valores necessarios para concretizar a reducao
    if direcao=='E':
        return -1,3,1,0,0
    elif direcao=='W':
        return 1,1,0,1,4
    elif direcao=='N':
        return 1,1,1,0,4   
    else:
        return -1,3,0,1,0   
                
                    

def zeros_entre_coord(tab,direcao,c,l):    #Recebe um tabuleiro a direcao e linha/coluna
    #A funcao recebe um tabuleiro, direcao, coluna e linha e elimina os zeros e
     # entre coordenadas
    
    if direcao == 'E' or direcao == 'W':  
        i, coluna, proximo, anterior, limite = quais_valores(direcao) 
        while coluna != limite:
            if tabuleiro_posicao(tab,cria_coordenada(l,coluna+proximo)) == 0 and \
               tabuleiro_posicao(tab,cria_coordenada(l,coluna+anterior)) != 0 :
                tab = elemina_zeros_esq_dir(tab,proximo,i,l,coluna,anterior)
                return zeros_entre_coord(tab,direcao,c,l)
            coluna = coluna+i
    
    else:
        
        i, linha, proximo, anterior, limite = quais_valores(direcao)
        while linha != limite:
            if tabuleiro_posicao(tab,cria_coordenada(linha+anterior,c)) == 0 and\
                tabuleiro_posicao(tab,cria_coordenada(linha+proximo,c)) != 0:
                tab = elemina_zeros_cima_baixo(tab,proximo,i,linha,c,anterior)
                return zeros_entre_coord(tab,direcao,c,l)
            linha = linha + i
            
    return tab


def elemina_zeros_esq_dir(tab,proximo,i,l,coluna,anterior):
    #Elimina zeros de acordo tendo em conta as colunas
    #Da esquerda para a direita ou da direita para esquerda, consoante a direcao
    #Esquerda para a direita se a jogada for W 
    
    while coluna >= 1 and coluna <= 4:
        tab = tabuleiro_preenche_posicao(tab,cria_coordenada(l,coluna+proximo),\
                tabuleiro_posicao(tab,cria_coordenada(l,coluna+anterior)))
        tab = tabuleiro_preenche_posicao(tab,cria_coordenada(l,coluna+anterior),0)
        coluna = coluna+i
        if coluna+anterior>4 or coluna+anterior<1 or coluna+proximo>4 or \
           coluna+proximo<1:
            break 
    return tab


def elemina_zeros_cima_baixo(tab,proximo,i,linha,c,anterior):
    #Elimina zeros de acordo tendo em conta as linhas 
     
    while linha >= 1 and linha <= 4:
        tab = tabuleiro_preenche_posicao(tab,cria_coordenada(linha+anterior,c),\
                tabuleiro_posicao(tab,cria_coordenada(linha+proximo,c)))
        tab = tabuleiro_preenche_posicao(tab,cria_coordenada(linha+proximo,c),0)
        linha = linha+i
        if linha + anterior >4 or linha + anterior <1 or linha + proximo >4 \
           or linha + proximo <1:
            break 
    return tab

#=================================================================#

#Reconhecedor      
def e_tabuleiro(t):
    """Recebe um argumento e devolve True caso o argumento seja do tipo tabuleiro e False caso contrario"""
    
    if isinstance(t,list) and len(t) == 5 and isinstance(t[4],int):
        for i in range(0,4):
            if not isinstance(t[i],list):
                return False
        for l in range(1,5):
            for c in range(1,5):
                if not isinstance(t[l-1][c-1],int):
                    return False
        return True
    
    else:
        return False
                
        
            
   
            
#Reconhecedor
def tabuleiro_terminado(tab):
    """Recebe um elemento do tipo tabuleiro e devolve True caso esteja terminado
        ou False caso nao esteja""" 
    #As copias dos tabuleiros sao feitas para evitar que o tabuleiro original seja
    #destruido
    t=copia_tabuleiro(tab)
    t1=copia_tabuleiro(t)
    t2=copia_tabuleiro(t1)
    t3=copia_tabuleiro(t2)
    
    if (len(tabuleiro_posicoes_vazias(tab))!=0):
        return False
    elif not tabuleiros_iguais(tabuleiro_reduz(t,"N"),tab):
        return False
    elif not tabuleiros_iguais(tabuleiro_reduz(t1,"S"),tab):
        return False
    elif not tabuleiros_iguais(tabuleiro_reduz(t2,"E"),tab):
        return False
    elif not tabuleiros_iguais(tabuleiro_reduz(t3,"W"),tab):
        return False
    else:
        return True
    

#Teste
def tabuleiros_iguais(tab1,tab2):
    """Recebe dois elementos do tipo tabuleiro e devolve True caso sejam 
    tabuleiros iguais"""
    
    for i1 in range(1,5):
        for i2 in range(1,5):
            if tabuleiro_posicao(tab1,cria_coordenada(i1,i2))!= \
               tabuleiro_posicao(tab2,cria_coordenada(i1,i2)):
                return False  # Verifica se se as coordenadas equivalentes tem o
                              #  mesmo valor
    if tabuleiro_pontuacao(tab1)!=tabuleiro_pontuacao(tab2): #se a pontuacao for
                                                              # diferente
        return False
    else:
        return True

#===============================================================================

def escreve_tabuleiro(tab):
    """Recebe um elemento do tipo tabuleiro e escreve no ecra a representacao
    externa do jogo 2048"""
    
    if not e_tabuleiro(tab) :
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    st = ''                     #string vazia para permitir imprimir o tabuleiro
    for l in range(1,5):
        for c in range(1,5):
            st = st+'[ '+str(tabuleiro_posicao(tab,cria_coordenada(l,c)))+' ]'+' '
        print (st)              #imprime cada conteudo da coordenada 
        st = ''
    print('Pontuacao:',tabuleiro_pontuacao(tab))

    
def pede_jogada():
    """Pede ao jogador uma direcao (N,S,E,W) e devolve uma cadeia de carateres 
    correspondente a coordenada"""
    
    jogada = True            #permite inicializar a variavel local "jogada" para
                             # ser possivel a sua inclusao num ciclo
    
    while jogada not in ("N","S","E","W"):
        
        jogada = input("Introduza uma jogada (N, S, E, W): ")
        if jogada in ("N","S","E","W"):        #se a jogadda for 
                                               # valida,interrompe o ciclo
            break
        else:
            print ("Jogada invalida.")
    return jogada
        

def copia_tabuleiro(tab):
    """Recebe um elemento do tipo tabuleiro e devolve uma copia deste"""
     
    copia_tab = cria_tabuleiro()
    
    #O ciclo cria um tabuleiro cujas coordenadas sao preenchidas com as 
    #coordenadas do tabuleiro
    
    for i in range(1,5):
        for i2 in range(1,5):
            copia_tab = tabuleiro_preenche_posicao\
                (copia_tab,cria_coordenada(i,i2),\
                 tabuleiro_posicao(tab,cria_coordenada(i,i2)))
    
            
    if tabuleiro_pontuacao(tab)!= 0:     
        copia_tab = tabuleiro_actualiza_pontuacao\
            (copia_tab,tabuleiro_pontuacao(tab))
    return copia_tab


def preenche_posicao_aleatoria(tab):
    """Recebe um elemento do tipo tabuleiro e preenche um posicao livre 
    aleatoria, com 2 ou 4"""
    
    posicoes_vazias = tabuleiro_posicoes_vazias(tab) #cria lista com posicoes 
                                                      # vazias
    if len(posicoes_vazias) == 0:                                                                
        return tab
    
    n_posicoes_vazias = len(posicoes_vazias)                                          
    num_random = 2000   #Inicializacao do ciclo while
    while num_random>=len(posicoes_vazias): 
        #enquanto o numero gerado for maior que o comprimento
        
        num_random=int(random.random()*16) #Se a posicao ja estiver preenchida,
                                            # preenche a seguinte

        
    dois_ou_quatro=random.random()  #Para escolher se vamos preencher com 2 ou 4
    if dois_ou_quatro>0.2:
        tab = tabuleiro_preenche_posicao(tab,posicoes_vazias[num_random],2)
               #das posicoes vazias, escolhe uma aleatoriamente 
                # atraves do numero aleatorio gerado
    else:                                                                                        
        tab = tabuleiro_preenche_posicao(tab,posicoes_vazias[num_random],4)
    return tab


def jogo_2048():
    """Permite jogar o jogo 2048"""
    
    tab = cria_tabuleiro()
    
    tab = preenche_posicao_aleatoria(tab)
    tab = preenche_posicao_aleatoria(tab)
    
    tab_novo = copia_tabuleiro(tab)
    escreve_tabuleiro(tab)
    while not tabuleiro_terminado(tab_novo):
        jogada = False
        while jogada not in ('N','S','E','W'):
            jogada=pede_jogada()
            tab_novo = copia_tabuleiro(tab)
            if jogada in ('N','S','E','W') and tabuleiros_iguais(tab,tabuleiro_reduz(tab_novo,jogada)):
                jogada = False
                print('Jogada Invalida')
                tab_novo = copia_tabuleiro(tab)
                
        tab=tabuleiro_reduz(tab,jogada)
        tab=preenche_posicao_aleatoria(tab)
        escreve_tabuleiro(tab)
        tab_novo=copia_tabuleiro(tab)