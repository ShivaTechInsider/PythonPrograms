def Fib(n):
        if(n==1):
            print(n)
        elif(n<=0):
            print("Not a Valid Number")
        else:
            a = 0
            b = 1 
            print(a)
            print(b)        
            for i in range(2,n):
              c = a+b 
              a = b
              b = c 
              print(c)
              
Fib(10)              