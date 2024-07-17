def checkPerfectSquare(n):
    return (int(n**0.5)**2) == n 

num = checkPerfectSquare(25)
print(num)
if(num==True):
    print("Perfect Square")
else:
    print("Not a Perfect Square")    