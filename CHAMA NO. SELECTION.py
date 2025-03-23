import random as rd
r=rd.sample(range(0, 6), 6)
x=[]
for si in r:
    p=r[si]
    x.append(p)

x.remove(0)
print(x)
cnt=1

getname=[]
for i in x:
    while True:
        
            name=str(input(f'\n{cnt}-Name Please!! ...AND PRESS ENTER: '))
            if name.strip():
                cnt+=1 
                getname.append(name)
                break
            else:
                print('\n     ERROR!!! \n\tPlease Enter You Name')    


for i in range(0, 5):
    print(f"\n{getname[i]} = {x[i]}")
    
            
