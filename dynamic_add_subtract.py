result=0
while(True):
 print("Your result is: ",result)
 print("Please select an option")
 print("1. add to result")
 print("2. Minus from result")
 print("3. exit from here")
 r=int(input("Your response: "))
 if r==1:
   result+=int(input("Please enter the number"))
 elif r==2:
   result-=int(input("Please enter the number"))
 else :
    print("you have successfully exited from the calculator")
    break

