def PrintPrimeNumbers(n):
    i = 2 
    primeList = []
    for i in range(2,n):
        count = 0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            primeList.append(i)
    return primeList


resultList = PrintPrimeNumbers(100)        
print(resultList)
                    
    
    
    