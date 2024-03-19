

def profile(name, age, place):
    txt ="my name is {}. Iam {} years old. Iam from {}."
    print(txt.format(name, age, place))
profile("pradeep", 21, "penagalur")

# ! Eg:4
# ? function with return statement

# 1.) a variable declared in side the functions can be accessed outside the function using return
# 2.) return does not print anything
# 3.) we cannot write any code below return statement


def f1():
    z = 8
f1()
print()

def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)



# 123
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::-1]
#    if string==rev:
#        print(n, "palindrome")
 #   else:
#         print("Not palindrome")  
#a = int(input("Enter the value:"))
#palindrome(a)


# ? based on the declaration of parameter and args
# ? functions are divided into 5 categories

# positional args
# keyword args
# defalut args
# variable length args
# keyword variable length args

# * positional args

# eg:1
def profile (name, phone, marks):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name, phone, marks))
profile(9346534034, "pradeep", 98) # unexpected output  

# * keyword args
# ! eg:2

# to overcome the disadvantages of position args, we use keyword args
# it is the process of initialising the paremeter with the args while caaling the functions
def profile (name, phone, marks):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name, phone, marks))
profile(name = "pradeep", marks = 98, phone=9346534034)


# todo ----> expection of keyword args function

def profile (name, phone, marks):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name, phone, marks))
#profile(name = "pradeep", ,9346534034, mark=98) # error ---> positional args follow keywords
#profile(9346534034, name="pradeep", mark=98) # error -->name has muitiple values

profile("pradeep", marks=98, phone=9346534034)


# * default args
# the 
# ! eg:1

def profile (name, phone, place="kadapa"):
    txt = "my name is {}. my phone number is {}. iam form {} plae."
    print(txt.format(name, phone, place))
    
profile("pradeep", 9346534034)

# eg:2
def profile (name, phone, place):
    if place == "Kadapa" or place=="KADAPA" or place == "kadapa":
        txt = "my name is {}. my phone number is {}. iam from {} plae."
        print(txt.format(name, phone, place))
    else:
        print("you are not eligable to sinnup")
profile("pradeep", 9346534034,"guntur")

# EXPECTION
#    if place == "Kadapa" or place=="KADAPA" or place == "kadapa":
#profile("pradeep", 9346534034)

#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.

#(*>#): positive integer
#(#>*): negative integer
#(#=*): 0
#Example 1:
#Input 1:

###***   -> Value of S
#0   → number of * and # are equal


# * varible length args
# ! eg:1
# to pass more than 1 arg to a paremeter means we use variable length  args
# to convert normal paremeter to variable length param, add * to their prefix of params

# name = "pradeep", "name2", "name3"
#def profile(name):
#    print("my name ", name)
#profile("pradeep", 'name2', 'name3')


# ! eg:2
# def profile(*name, age):
#    for val in name:
#        print("my name is ", val," my age is", age)
# profile( "pradeep", 'name2', 'name3', 21)



# def profile(age, *name):
#    for val in name:
#        print("my name is ", val," my age is", age)
# profile(21, "pradeep", 'name2', 'name3')


# * keyword variable length args
# ! eg:1

#def price(price_list):
 #   print(price_list)
#print()

d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)


#1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



n = 5
{1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input(" enter the number: "))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)

#n = int(input(" enter the number: "))
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)

# ! -------> object orientd programming


# the paradigms of objects oriented programming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! class is a blue print of an object
l1 = [1,2,3,4,5,6,]

# ? eg:1
class c1:
    name = "pradeep"
    print(name)

# ? eg:2
class person:
    name = "as"
c = person()
print(c.name)


# c = person() # c or object
# the process of creation of an object is called as instantiation
# print(c.name)


# ? eg:3
# created of amethod
# when the function is created with a class is called as method

class person:
    def display(person):
        print('hello welcome to classes')
p = person()
p.display()


# ? eg:4
# ! method with parameter

class person:
    def display(person, name, age):
        print(name, age)
p = person()
p.display("as",21)


# ! eg:5

class person1:
    fname = "as"
    lname ="pr"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p = person1()
p.first_name()
p.full_name()
    
    
# ? eg:6
class profile:
    def __init__(self):
        print("hey")
p = profile()
    
  

    

    

























