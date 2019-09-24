#Write a simple interest calculator
#Si = P*T*R/100


p = float(input("Enter principal amount: "))
t = float(input("enter time period: "))
r = float(input("Enter rate of interest: "))

Si=p*t*r/100
print("Simple interest is: ", Si)