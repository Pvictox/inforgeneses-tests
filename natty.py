def fibonnaci(num:int)->None:

    if(num==0): print("0")
    if(num==1): print("1")

    memo = [0] * (num+1)
    memo[0] = 0
    memo[1] = 1
    print(memo[0], end=" ")
    print(memo[1], end=" ")
    for i in range(2, num+1):
        memo[i] = memo[i-1]+memo[i-2]
        print(memo[i], end=" ")
    

fibonnaci(40)