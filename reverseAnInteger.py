a=str(input("Type an integer "))
lenth=len(a)
print("The inverse of ",a," is ",end="")
for k in range(1,lenth+1):
   print(a[-k],end="")
'''
The below optiona also can inverse the integer as that is a string
print("\n\n Using array index moving system ", a[::-1])
'''
