import operator as op
class person :
    def __init__(self,name):
        self.name = name
class sum1 :
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
        
    def work(self):
        s = op.add(self.a, self.b)
        print("Total " + str(s)) 
y = person("John")
print(y.name)
w = sum1 (1,2)
print(w.a)
print(w.b)
print ("\n")
w.work()
        