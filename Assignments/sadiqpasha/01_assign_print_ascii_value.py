#WAP to input a string and print ascii value of each character

i =0
st = input("Enter a string: ")
while i<len(st):
    print(ord(st[i]))
    i=i+1