import math 
degree = float(input("Enter the degree: "))
signnn = input("Choose sin/cos/tan: ")

if signnn == "cos":
    print(math.cos(degree))
    
elif signnn == "sin":
    print(math.sin(degree))
    
elif signnn == "tan":
    print(math.tan(degree))
    
else:
    print("Bro enter the valid signs! ")
            