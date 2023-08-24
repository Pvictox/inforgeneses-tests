import operator

'''
    Complexidade: O(n^2) 
    TODO: Verificar meios de otimização
'''
# 1) Inicializar a matriz com as corridas

numCorridas, quantPilotos = 1,1 #Inicialização das variáveis que servirão como controle do meu loop.
result = [] #Lista de resultados que serão mostradas ao final do codigo.
numCorridas, quantPilotos = [int(i) for i in input().split()] #Leitura dos valores 'G' (num. corridas) e 'P' (quant de pilotos)
while (numCorridas != 0 and quantPilotos != 0):
    matrizCorridas = []
    for i in range(numCorridas):  #Decidi colocar as corridas em uma matriz. Este loop serve para popular a mesma com as entradas referentes à corrida.
        matrizCorridas.append([])
        matrizCorridas[i] = [int(i) for i in input().split()] 
    dicionarioPilotos = dict() #Cada pontuação dos participantes da corrida ficarão em um dicionário.
    '''
        E.g: 
            Chave (representa o corredor) : (pontuação)
                        1  : 0
                        2  : 0
                        3  : 0 
    '''
    for i in range(1, quantPilotos+1):
        dicionarioPilotos[i] = 0 #Inicializo as chaves sendo que cada uma irá ter 0 pontos (Ainda não foi calculado a corrida)
    quantSistemaPontu = int(input()) #Quantidade de sistemas de pontuação que serão passados como dado.
    for i in range(quantSistemaPontu):
        dicionarioPilotos = dicionarioPilotos.fromkeys(dicionarioPilotos, 0) #Importante: A cada calculo do sitema de pontuação o dicionário de pontos deve ser RESETADO. Esta linha faz isso setando os valores de cada corredor para 0. 
        vetorPont = [int(i) for i in input().split()] #Lendo a pontuação daquele respectivo sistema de pontuação
        limiteAgracidados = vetorPont.pop(0) #Retiro o primeiro elemento da lista lida anteriormente. Dessa forma eu possuo um controle a respeito de quantos corredores receberão os pontos.
        for i in range(len(matrizCorridas)): #Percorro a matriz de corridas
            for j in range(len(matrizCorridas[i])):
                if (matrizCorridas[i][j] <= limiteAgracidados): #Se a posição daquele respectivo corredor [i][j] for <= a quantidade de corredores que receberão pontos, isso indica que este mesmo corredor receberá os pontos.
                    '''
                        e.g: Temos 2 corredores (Corredor 1 e Corredor 2) e 1 corrida só. Nossa matriz seria algo do tipo:
                                  M =  2 || 1  (1 linha e 2 colunas) => (1 corrida e 2 corredores)
                             Caso o nosso sistema de pontuação fosse assim: S = [1,10] indicaria que apenas 1 corredor (S[0]) receberia os pontos e que o primeiro colocado receberia 10 pontos(S[1]).
                             Observe que nesse caso, o corredor da posição M[0][0] da matriz não receberia os pontos pq 2 não é MENOR OU IGUAL A 1. 
                    '''
                    dicionarioPilotos[j+1] += vetorPont[ matrizCorridas[i][j] - 1] #Atualizo a pontuação do corredor.
        sortDict = ( sorted( dicionarioPilotos.items(), key= operator.itemgetter(1), reverse=True) ) #ORDENO O DICIONÁRIO DE ACORDO COM A PONTUÇÃO (Decrescente)
        strResult = "" 
        for elemento in sortDict:
            if (elemento[1] == sortDict[0][1]): #Comparo a pontuação de um determinado corredor com a pontuação do primeiro. Observe que aqui eu estou usando o dicionario ordenado do maio para o menor então o primeiro corredor sempre terá a maior pont.
                strResult+= f"{elemento[0]} " 
            else: break
        result.append(strResult) #Adiciono a string de resultado no vetor
        vetorPont.clear() #Limpo as estruturas usadas, preparando-as para o próximo conjunto de dados (se houver)
        sortDict.clear()
    dicionarioPilotos.clear()
    numCorridas, quantPilotos = [int(i) for i in input().split()]

for elemento in result:
    print(elemento) #Imprimo o resultado final
    