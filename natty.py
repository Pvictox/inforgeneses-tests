def fibonnaci(num:int)->None:
    '''
        Função que imprime a seq. de fibonnaci até um valor 'num'

        Arguments:
        num -- valor inteiro que representa até qual i-ésimo termo a sequência printará.

        Complexidade: O(n)

        Observação: Esta função pode ser fácilmente modificada para retornar um elemento x da seq. de fibonnaci.
    '''
    if(num==0): print("0")
    if(num==1): print("1")

    memo = [0] * (num+1)  #Variável de memorização dos valores da sequência
    memo[0] = 0  #Valores conhecidos da sequência (primeiro e segundo termo)
    memo[1] = 1
    print(memo[0], end=" ")
    print(memo[1], end=" ")
    for i in range(2, num+1):
        memo[i] = memo[i-1]+memo[i-2] #Cálculo do próximo termo sendo a soma dos 2 anteriores.
        print(memo[i], end=" ")
    
    #Caso quiséssemos retornar o 23º elemento da sequência poderíamos simplemente dar um 'return memo[23]'

fibonnaci(40)