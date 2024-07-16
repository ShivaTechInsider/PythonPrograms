# Find out common letters bewtween two Strings
# eg 1)  NAINA
#    2) REENE  
#  output should be .....   "N"   

a = "NAINA"
b = "REENE"

a = set(a)
b = set(b)

print(a.intersection(b))