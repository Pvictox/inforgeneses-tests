def iziSolver()->None:
    '''
        Imprime 'Fizz' caso o respectivo valor de 'i' for múltiplo de 3.
        Imprime 'Buzz' caso o respectivo valor de 'i' for múltiplo de 5.
        Imprime 'FizzBuzz' caso o respectivo valor de 'i' for múltiplo de 5 E de 3 ao mesmo tempo.
        Imprime o valor de 'i' caso contrário.
    '''
    for i in range(1,51):
        if (i%3 == 0 and i%5==0): print("FizzBuzz")
        elif (i%3 == 0): print("Fizz")
        elif(i%5==0): print("Buzz")
        else:
            print(str(i))

iziSolver()