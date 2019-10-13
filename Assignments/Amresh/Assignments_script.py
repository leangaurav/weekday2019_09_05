#(1)AssignExtra1-Input,TypeConversion

#1. Input temperature in Fahrenheit in print in Celsius.
tep = int(input("Enter A tempurtre in Fahrenheit:"))
cel = (5/9.0)*(tep -32)
print(cel)
"""Enter A tempurtre in Fahrenheit:4
-15.555555555555557"""

#2Write a program to input a number and print its square and cube.
a = int(input('Enter a Number:-'))
s = a*a
d = a*a*a
print("Square of given number is:-", s)
print("cube of given number is:-", d)

"""Enter a Number:-2
Square of given number is:- 4
cube of given number is:- 8"""

#3WAP to input a number n and a number m and print the result of following
n = int(input('Enter a Number:-'))
m = int(input('Enter a Number:-'))
n1 = n*n
print(n1)
m2 = m*m
print(m2)
m3 = n1+m2
print(m3)

"""Enter a Number:-2
Enter a Number:-10
4
100
104"""

#4WAP to input a numbers M and N and print result of MN. (use both ** and pow)
m = int(input('input a numbers M and print result of MN:-'))
n = int(input('input a numbers N and print result of MN:-'))
mm = m**m
nn = n**n
mn2 = pow(m,n)
        
print(mm)
print(nn)
print(mn2)
"""input a numbers M and print result of MN:-2
input a numbers N and print result of MN:-3
4
27
8"""

dir(pow)
"""['__call__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__name__',
 '__ne__',
 '__new__',
 '__qualname__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__self__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__text_signature__']"""
 
 #5Write a simple interest calculator.
p = int(input('Enter Principle Amount:-'))
t = int(input('Enter Time:-'))
r = int(input('Enter Rate of Interest:-'))
s = (p * t * r)//100
print("Simple Interest is:-", s)
"""Enter Principle Amount:-2000
Enter Time:-2
Enter Rate of Interest:-5
Simple Interest is:- 200"""

#7WAP to print sum of first n natural numbers. (n needs to be taken as input).
n = int(input('Enter n Number:-'))
sn = n*(n+1) / 2
print('Sum of n number:-', sn)
"""Enter n Number:-345
Sum of n number:- 59685.0"""

#8WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and also the pythonic way).
n1 = int(input('Enter First Number:-'))
n2 = int(input('Enter Second number:-'))
print()
tem = 0
tem = n2
n2 = n1
n1 = tem
print('After swap:-' ,n1,n2)
"""Enter First Number:-123
Enter Second number:-234

After swap:- 234 123"""

#9WAP to print ascii value of all white-space characters present in python.
n = input('Enter A white-space characters:-')
ac = ord(n)
print(ac)

"""Enter A white-space characters:- ' '
32"""


#10WAP that takes area of a circle and gives back the radius and circumference
import math 
math.pi
area = float(input('Enter area :')) 
print("Radius :",((area)/math.pi)**0.5)
print("Circum :",(2*math.pi)*(((area)/math.pi)**0.5))

"""Enter area :23
Radius : 2.7057581899030048
Circum : 17.00078010357939"""


#11We need to input marks in 5 subjects out of 100 and print percentage
s1 = int(input("Enter1st marks:-"))
s2= int(input("Enter 2stmarks:-"))
s3= int(input("Enter 3rd marks:-"))
s4 =int(input("Enter 4st marks:-"))
s5= int(input("Enter 5th marks:-"))
print(((s1+s2+s3+s4+s5)/(5*100))*100)

"""Enter1st marks:-34
Enter 2stmarks:-45
Enter 3rd marks:-65
Enter 4st marks:-75
Enter 5th marks:-56
55.00000000000001"""

#(2) AssignmentPython1-Intro
#1. Predict Output:
s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
print( len(s1), len(s2))
#6 19

#2. WAP to input a string and print its length.
s = input('Enter a String:-')
print(len(s))
"""Enter a String:-amresh
6"""

#3. WAP to input 2 numbers and print their sum and difference.
n1 = int(input('Enter first number:-'))
n2 = int(input('Enter Second number:-'))
sm = n1+n2
d = n1-n2
print('Sum of two no:-', sm)
print('Difference of two no:-', d)
"""Enter first number:-20
Enter Second number:-30
Sum of two no:- 50
Difference of two no:- -10"""


#4. Predict output:
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)
#abde

#6. Predict output:
s1 ='ab' * 4
print(s1)
#abababab

#7. Predict output:
s1 = 'ab''\n'* 4
print(s1)
"""ab
ab
ab
ab"""

#8. WAP to input a string s and a number n. Print the string n times on the screen, each should
#appear in a separate line (do not use any kind of loops, use the multiplication operator).
s = input('Enter a String:-')
n = int(input('How many time you want to print:-'))
c = s +'\n'
s1 = (c*n)
print(s1)

"""Enter a String:-amresh
How many time you want to print:-4
amresh
amresh
amresh
amresh"""

#9. Predict Output:
res = print('Amresh')
print(res)
"""Amresh
None"""

#10. Predict Output:
res = len('tuteur.py@gmail.com')
print(type(res))
#<class 'int'>

#11. Predict Output:
s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1 +'\n'+ s2
print(s3)
print(type(s3))
print(len(s3))
"""Gaurav
tuteur.py@gmail.com
<class 'str'>
26"""

#12. Find the name of function to find the square root. (see all the options available in dir() of math)
import math
print(dir(math))
#math.sqrt()

#13. WAP to input a number and print its square root ().
import math
n = int(input("Enter A number:-"))
s = math.sqrt(n)
print(s)
"""Enter A number:-2
1.4142135623730951"""

#14WAP to input 4 numbers from user and print their average
n1 =  int(input('Enter Four number:-'))
n2 = int(input())
n3 = int(input())
n4 = int(input())
sum_n = (n1+n2+n3+n4)/4
print(sum_n)
"""Enter Four number:-2
3
4
5
3.5"""

#15. Use the help function to check what the abs function in python does.
help(abs)
"""Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
"""

#16. What is the output of this code when run from python interpreter.
print(__name__)
#__main__

#17. What is the output of this code when run from a python script.
print(__name__)
"""Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument."""
  
#18. Does the dir of int class contain an attribute __name__ (Y/N)
dir(int)
#NO
    
#19. Predict the output of:
print(__name__)
print(__builtins__)
print(int.__name__)
"""__main__
<module 'builtins' (built-in)>
int"""

#7Predict output:
s1 = 'ab\n' * 4
print(s1)

#8. WAP to input a string s and a number n. Print the string n times on the screen, each should
#appear in a separate line (do not use any kind of loops, use the multiplication operator).
s = input('Enter a String:-')
n = int(input('How many time you want to print:-'))
c = s +'\n'
s1 = (c*n)
print(s1)

#9. Predict Output:
res = print('Amresh')
print(res)

#10. Predict Output:
res = len('tuteur.py@gmail.com')
print(type(res))

#11. Predict Output:
s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1 +'\n'+ s2
print(type(s3))
print(len(s3))
#math.sqrt()

#13. WAP to input a number and print its square root ().
import math
n = int(input("Enter A number:-"))
s = math.sqrt(n)
print(s)

#14WAP to input 4 numbers from user and print their average
n1 =  int(input('Enter Four number:-'))
n2 = int(input())
n3 = int(input())
n4 = int(input())
sum_n = (n1+n2+n3+n4)/4
print(sum_n)

#15. Use the help function to check what the abs function in python does.
help(abs)
"""Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument."""

#16. What is the output of this code when run from python interpreter.
print(__name__)
#__main__

#17. What is the output of this code when run from a python script.
print(__name__)
"""Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument."""
 
#18. Does the dir of int class contain an attribute __name__ (Y/N)
dir(int)
#NO

#19. Predict the output of:
print(__name__)
print(__builtins__)
print(int.__name__)
"""__main__
<module 'builtins' (built-in)>
int"""
# AssignmentPython2- Strings

#1. Guess output of each slice:
s = "Python is Object Oriented"
print(s[-1]) 
print(s[::-1])
print(s[:-1])
print(s[1:1]) 
print(s[4:10])

"""d
detneirO tcejbO si nohtyP
Python is Object Oriente

on is """

#2. What error do you see for following statements:
#s= ‘’
#s = ''
#print(s[1])
"""File "<ipython-input-71-55cc7f7875fc>", line 2
    s= ‘’
        ^
SyntaxError: invalid character in identifier
"""
#3. Do you get any error for the following code, if not give the output:
#S=‘Gaurav’
#print(s[1])
"""  File "<ipython-input-75-21f5d90cdb2a>", line 2
    S = list(‘Gaurav’)
                    ^
SyntaxError: invalid character in identifier
"""
s = 'Gaurav'
print(s[1])
#a

#4. Find output of the following:
#**********************************
"""A(Wrong)

s=‘a b cd’
print(len(s))
print(s[::2])
print(len(s[::2]))
 File "<ipython-input-79-bcd1c6e8825a>", line 2
    s=‘a b cd’
       SyntaxError: invalid character in identifier
"""
#A Correct
s='a b cd'
print(len(s))
print(s[::2])
print(len(s[::2]))
"""6
abc
3"""
#**********************************
"""B(Wrong) 

s=‘a#b#c#d#’
print(s.split())
print(s.split(‘#’))
l=s.split(‘#’)
s=‘$’.join(l)
print(s)"""

#B Correct
s='a#b#c#d#'
print(s.split())
print(s.split('#'))
l=s.split('#')
s='$'.join(l)
print(s)
"""['a#b#c#d#']
['a', 'b', 'c', 'd', '']
a$b$c$d$"""
#**********************************
"""C(Wrong)
S=‘Gaurav’
S=S[::-2][::-2]
print(S)
File "<ipython-input-88-0c08b8d902c6>", line 43
    S=‘Gaurav’
             ^
SyntaxError: invalid character in identifier"""
#C Correct 
S='Gaurav'
S=S[::-2][::-2]
print(S)
#av
#**********************************
#D (Wrong) 
print(1>2)
#False
#D Correct
print(1<2)
#True
#**********************************
"""E(Wrong)
print(4%2, 5%2, 2%5, sep=‘, ’)
 File "<ipython-input-92-35e512997e0f>", line 64
    print(4%2, 5%2, 2%5, sep=‘, ’)
                             ^
SyntaxError: invalid character in identifier"""
##D Correct
print(4%2, 5%2, 2%5, sep=',' )
#0,1,2
#**********************************
"""#E(Wrong)
s=‘abcba’
s.upper()
print(s)
print(s.count(‘A’), end = ‘ ,’)
print(s.count(‘A’, 2,4) , end = ‘ ,’)
print(s.count(‘a’, 2,4) , end = ‘ ,’)
 File "<ipython-input-94-92dbd0c380dc>", line 74
    s=‘abcba’
            ^
SyntaxError: invalid character in identifier"""
##E Correct
s='abcba'
s.upper()
print(s)
print(s.count('A'), end = ',')
print(s.count('A', 2,4) , end = ' ,')
print(s.count('a', 2,4) , end = ' ,')
#abcba
#0,0 ,0 ,
#**********************************

#5. WAP to input a string and remove all spaces from it.
s = input('Enter a String:-')
a = s.split()
print(a)
"""Enter a String:-am re sh
['am', 're', 'sh']"""

#6What does this symbol denote:
[]
#[]

import string
#7. WAP to print all methods(functions/operations) available in a string (Hint : dir())
dir(string)
"""['Formatter',
 'Template',
 '_ChainMap',
 '_TemplateMetaclass',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_re',
 '_string',
 'ascii_letters',
 'ascii_lowercase',
 'ascii_uppercase',
 'capwords',
 'digits',
 'hexdigits',
 'octdigits',
 'printable',
 'punctuation',
 'whitespace']"""
#8. Write statement to check if rstrip method is available in the str class.
#(Hint : Use the find function or 
a = 'rstrip'
a in dir(str)

#9. WAP to store the following patterns in a string variable and then print them:
s = """\t*********
          * 
          *
          *
          *
          *"""
print(s)
s1 = """*\t\t*
*  *   *   *    *
*      * \t*
*      *        *
"""
print(s1)
s3 = """\t____________
        |           |
        O           |
       /|\          |
       / \          |
                    |
        ____________"""
print(s3)

#10. WAP to input a string and replace all space with new lines (\n) and print again.
s = input('Enter a String:-')
s1 = s.replace(' ','\n')
print(s1)
"""Enter a String:-a s v
a
s
v"""
#11. WAP to input complete name(first and last name separated by space) and print first and last
#name separately along with their length in upper case.
name1 = input('Enter First name:-').split(' ')
name2 = input('Enter last name:-').split(' ')
n = len(name1)
n2 = len(name1)
print(n)
print(n2)
"""Enter First name:-amresh kumar
Enter last name:-singh
2
2"""

#12. WAP to input a string and split it into 2 halves. The string can be of any length
St = input("Enter the String :")
lenght = len(St)
S1 = St[0:round(lenght / 2)]
S2 = St[round(lenght / 2):]
print(S1," ", S2)
"""Enter the String :amreshsingh
amresh   singh"""
#AssignmentPython3-FunctionsIntro
#1. WAP to input 2 strings and swap the strings 
def swap_String():
    s = input("Enter the first String:")
    s1 = input("Enter the second String:-")
    tem =0
    temp = s1
    s1 = s
    s = temp
    print(temp,s1)
swap_String()
"""Enter the first String:amresh
Enter the second String:-singh
singh amresh"""
    
#2.WAP to generate 4 random numbers in the range 0-26 and print their average
import random
def p_avg():
    n =random.randint(0,26)
    avg = n/4
    print(avg)
p_avg()

#4. WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple Interest.
def get_si():
    p = int(input('Enter Principle Amount:-'))
    t = int(input('Enter Time:-'))
    r = int(input('Enter Rate of Interest:-'))
    s = (p * t * r)//100
    print("Simple Interest is:-", s)
get_si()
"""Enter Principle Amount:-2000
Enter Time:-2
Enter Rate of Interest:-4
Simple Interest is:- 160"""

"""5. WAF get_amount() that takes Principle, Rate and Time as arguments and returns the
Total amount using the get_si() function from above to calculate the SI. Also provide
Rate = 10 and Time = 1 as default arguments."""
def get_amount():
    r1=10
    t2=1
    print('Rate:',r1)
    print('Time:',t2)
    def get_si():
        p = int(input('Enter Principle Amount:-'))
        t = int(input('Enter Time:-'))
        r = int(input('Enter Rate of Interest:-'))
        s = (p * t * r)//100
        print("Simple Interest is:-", s)
get_amount()         
get_si()
"""Rate: 10
Time: 1
Enter Principle Amount:-2000
Enter Time:-2
Enter Rate of Interest:-4
Simple Interest is:- 160"""

#6. WAP get_ci() that takes Principle, Rate and Time as arguments and returns the Compound Interest.
def get_ci():
    p = int(input('Enter Principle Amount:-'))
    t = int(input('Enter Time:-'))
    r = float(input('Enter Rate of Interest:-'))
    ci = p * (pow((1 + r / 100), t)) 
    print("Compound Interest is:-", ci)
get_ci()
"""Enter Principle Amount:-2000
Enter Time:-3
Enter Rate of Interest:-4.5
Compound Interest is:- 2282.3322499999995"""

#9. WAP to input number of seconds and print in days, hours, minutes and seconds
#ex: input = 10000
#Output = 0 day 2 hour 46 minute 40 second
sec= int(input("Enter Seconds"))
def convert_sec(sec):
    mint = sec/60
    hour = mint/60
    d = hour/24
    print(d," Days",hour," hour",mint," minute",sec,"seconds")

convert_sec(sec)
"""Enter Seconds120
0.001388888888888889  Days 0.03333333333333333  hour 2.0  minute 120 seconds"""
#10. Check your version of python interpreter without opening the interpreter (Which
#command needs to be used on the command line).
#python.exe

#11. Find output:
x = 2
x *=3
x = x%4
y = -x
print(x,y)
#2 -2"""

#12. Find output:
def funct():
    pass
print(funct())
#None
# AssignmentPython4-List,Tuple
#1. Convert a Tuple t = (1,2,3,4,5) to a list
t= (1,2,3,4,5)
a=list(t)
print(t)#tuple
print(a)#list
#[1, 2, 3, 4, 5]
#2. WAP to join a list and a tuple:
L = [1,3,5,7]
T = (8,6,4,2)
L.append(list(T))
print(L)
#4. Print the list in reverse order
#l = [‘a’, ‘d’, ‘c’, ‘A’, ‘C’]
l = ['a','d','c','A','C']
l.reverse()
l
#['C', 'A', 'c', 'd', 'a']
#5. Print Elements at Odd indexes from a list (Do not use loop)
l = [10,11,20, 21,30, 31, 40, 41]
l[1:len(l):2]
#[11, 21, 31, 41]
#6. How many ways you can copy a list.
#-- copy a list by slicing - example (b = a[:])
#-- variablename.copy()
#7. Predict output
n_list = ["Happy",[2,0,1,5]]
print(n_list[0][1])
print(n_list[1][3])
#a
#5
#8. Predict output
odd =[2,4,6,8]
odd[0]=1
print(odd)
odd[1:4]=[3,5,7]
print(odd)
#[1, 4, 6, 8]
#[1, 3, 5, 7]
    


