
def mostraMatriz(mat:list)->None:
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end= " ")
        print("")

# 1) Inicializar a matriz com as corridas

numCorridas, quantPilotos = 1,1

while (numCorridas != 0 and quantPilotos != 0):
    print("Digite")
    numCorridas, quantPilotos = [int(i) for i in input().split()]
    matrizCorridas = []
    for i in range(numCorridas):
        matrizCorridas.append([])
        matrizCorridas[i] = [int(i) for i in input().split()] 
    
    mostraMatriz(mat=matrizCorridas)