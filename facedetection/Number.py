def getmin(set):
    min = set[0]
    i=1
    while(i>5):
        if(min>set[i]):
            min =set[i]
            i=i+1
    return min

def getmax(set):
      max = set[0]
      i = 1   
      while( i < 5 ):
       if( max <  set[i] ):
               max = set[i]
      
               i = i + 1    
      return max
set1 = [1,2,3,4,5]
set2 = [10,20,30,40,50]

min=getmin(set1)
print("min in first set", min)
min=getmin(set2)
print("min in second set", min)

max = getmax(set1)
print ("Max in first set = ", max)
    
# Now process second set of numbers available in set2[]
max = getmax(set2)
print ("Max in second set = ", max)