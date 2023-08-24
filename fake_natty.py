import operator

def mostraMatriz(mat:list)->None:
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end= " ")
        print("")

# 1) Inicializar a matriz com as corridas

numCorridas, quantPilotos = 1,1
result = []
numCorridas, quantPilotos = [int(i) for i in input().split()]
while (numCorridas != 0 and quantPilotos != 0):
    matrizCorridas = []
    for i in range(numCorridas):
        matrizCorridas.append([])
        matrizCorridas[i] = [int(i) for i in input().split()] 
    dicionarioPilotos = dict()
    for i in range(1, quantPilotos+1):
        dicionarioPilotos[i] = 0
    quantSistemaPontu = int(input())
    for i in range(quantSistemaPontu):
        dicionarioPilotos = dicionarioPilotos.fromkeys(dicionarioPilotos, 0)
        vetorPont = [int(i) for i in input().split()]
        limiteAgracidados = vetorPont.pop(0)
        for i in range(len(matrizCorridas)):
            for j in range(len(matrizCorridas[i])):
                if (matrizCorridas[i][j] <= limiteAgracidados):
                    dicionarioPilotos[j+1] += vetorPont[ matrizCorridas[i][j] - 1]
        sortDict = ( sorted( dicionarioPilotos.items(), key= operator.itemgetter(1), reverse=True) )
        #print(str(sortDict))
        strResult = ""
        for elemento in sortDict:
            if (elemento[1] == sortDict[0][1]):
                strResult+= f"{elemento[0]} "
            else: break
        result.append(strResult)
        vetorPont.clear()
        sortDict.clear()
    dicionarioPilotos.clear()
    numCorridas, quantPilotos = [int(i) for i in input().split()]

for elemento in result:
    print(elemento)
    