def calculate (L = None, w = None, h = None, ):
    if L != None and w != None and  h == None :
        print('Area: ' + str(L*w))
    else:
        print('Volume: ' + str(L*w*h))  
choose = str(input('want to calculate Volume or Area?: '))  
if choose.lower() == 'volume':
    dimen = []
    for i in range (3):
        dim = int(input('Enter dim and PRESS ENTER: '))
        dimen.append(dim)
    lng = dimen[0]
    wid = dimen[1]
    heg = dimen[2]
    calculate(lng, wid, heg)
else:
    dimen = []
    for i in range (2):
        dim = int(input('Enter dim and PRESS ENTER: '))
        dimen.append(dim)
    lng = dimen[0]
    wid = dimen[1]
    calculate(lng, wid)    
    
         
 
    
#ANSI