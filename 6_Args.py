def add(*args):           ## it will access it as a tuple (2,3) and (3,5,8)
    s = 0 
    for i in args:
        s += i 
    print("the sum of numbers is ",s)
    
    
add(2,3)
add(3,5,8)     
   



# def add(*args,name):           ## it will access it as a tuple (2,3) and (3,5,8)
#     s = 0 
#     for i in args:
#         s += i 
#     print("the sum of numbers is ",s)
#     print(name)
    
# add(2,3,name="shiva")