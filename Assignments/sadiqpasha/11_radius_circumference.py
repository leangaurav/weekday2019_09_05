#WAP that takes area of a circle and gives back the radius and circumference

import math
A = float(input("Enter area of circle: "))
r = math.sqrt(A/3.141)
c = 2*3.141*r
print("radius is : ", r)
print("circumference is : ", c)