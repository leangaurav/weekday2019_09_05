#Input Principal, Rate, Time and print Compound Interest and Amount
"""Compound interest for principal:
P(1+r/n)(nt) 
#The formula for compound interest, including principal sum, is:
#A = P (1 + r/n) (nt)

"""

import math

p = float(input(" Please Enter the Principal Amount : "))
r = float(input(" Please Enter the Rate Of Interest   : "))
t = float(input(" Please Enter Time period in Years   : "))

ci = p * (math.pow((1 + r / 100), t)) 
compound_int = ci - p

print("Future Compound Interest for Principal Amount {0} = {1}".format(p, ci))
print("Compound Interest for Principal Amount {0} = {1}".format(p, compound_int))
