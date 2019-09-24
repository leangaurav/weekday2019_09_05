#WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and
#also the pythonic way).

n = int(input("Enter a num: "))
m = int(input("Enter another num: "))

print("values of n and m before swap: ", n, m)
temp = n
n = m
m = temp

print("values of n and m after swap are: ", n, m)
n,m = m,n
print("in pythonic way: values of n and m are: ", n,m)