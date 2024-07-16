# Move the zeroes to the end of the list

a = [1,0,2,3,0,4,5]

for i in a:
    if(i==0):
        a.remove(i)
        a.append(i)
        
print(a)        