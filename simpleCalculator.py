print("Input 2 number")
p,q=map(int,input().split())
def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def mul(a,b):
   return a*b
def div(a,b):
   return a/b
w=add(p,q)
x=sub(p,q)
y=mul(p,q)
z=div(p,q)

print("sum =",w,"\n Difference=",x,"\nMultiplication =",y,"\n Division=",z)
