fn=input ("Enter your first name: ")
sn=input ("Enter your second name: ")
yr=input ("Enter your year pf birth: ")
age=(str(int(2023)-int(yr)))
print(sn+' '+fn+" "+"\nAge: "+age )
if(int(age)<18):
    print("Minor")
else:
    print (input ("What course you wish to taking: "))
 
