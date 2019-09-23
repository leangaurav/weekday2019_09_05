#WAP to input a string and find the sum of ascii value of all characters

i =0
s= 0
st = input("Enter a string: ")
while i<len(st):
    print((ord(st[i])))
    s =s+(ord(st[i]))
    i=i+1
print("sum: ", s)