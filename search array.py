x= [12,24,45,34,16,25]
searchValue=(int(input("Enter the value you wish to search ")))
for w in range (0, 6):
    if(x[w] == searchValue):
        print ((str(searchValue)) + " is present at location " + (str(w+1)))
        break
if(searchValue != x[w]):  
    print((str(searchValue)) + "is not present in the array")
          
    