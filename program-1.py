class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
a=int(input())
b=int(input())
operations=input()
result=calculator(a,b)
if (operations=="+"):
    print("Addition:",result.add())
elif (operations=="-"):
    print("Subtraction:",result.sub())
elif (operations=="*"):
    print("Multiplication:",result.mul())
elif (operations=="/"):
    print("Division:",result.div())