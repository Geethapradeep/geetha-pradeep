
s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
n1 = 0
n2 = 1
ans = 0+1

n1 = 1
n2 = 2
ans = 1+2

n1 = 2
n2 = 3
ans = 2+3

# ! find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1
for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)

# ! constructors
# ? eg:1
# unparametarised constructor

class profile:
    def __init__(self):
        print("hello world")
obj = profile()
obj.__init__()

# ? eg;2

#parameterised constructor
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)
obj = profile(1, "pradeep", 21)

# ? eg:3
class c1:
   email = "agpradeep@gmail.com"
   def m1(self):
         name ="pradeep"
         place = "as"
         print(name, place)
         print(self.email)
obj = c1()
obj.m1()

# ? eg:4
##class c1:
##    def m1(self):
##        name = "pradeep"
##        age =22
##        return name, age
##    def display(self):
##        #print(self.name, self.age)
##        print(self.m1())
##object = c1()
##object.display()

# ? eg:5
# ! to use the variable inside the constructor in another methods
class class1:
    
    def __init__(self):
        self.name = "raja mama"
        self.email = "kraja@gmail.com"
    def display(self):
        print(self.name, self.email)
c1 = class1()
c1.display()
        
# ! ------> inheritance
# the process of utilising the methods and attributes of parent class throught the object of child claass it is called as inheritance

# 5 types of inheritance
# single inheritance
# muitilevel inheritance
# hybrid inheritance
# herarichal inheritance

# ! single inhertiance

# it has only one parent class and only one child class
# ? eg:1
class parent:
    def m1(self):
        print(" Iam parent class")
class child(parent):
    def m2(self):
        print(" Iam child class")

obj = child()
obj.m1()

# ? eg:2
class c1:
    def ___init__(self):
        print("Iam constructor from parent class")
class child1(c1):
    pass
obj = child1()
    

# ? eg:3
class parent:
    name = " ramesh mama"
class child(parent):
    def display(self):
        print(self.name)
d = child()
d.display()


# ? eg:4

# ! multilevel inheritance
# ? eg:1
class voice:
    def sound(self):
        print(" all the animals have their own voices")

class dog(voice):
    def dog__voice(self):
        print("bark")

class cat(dog):
    def cat__voice(self):
        print("meow")

class parrot(cat):
    def parrot__voice(self):
        print("speak")

all = parrot()
all.dog__voice()  
all.cat__voice()
all.sound()
all.parrot__voice()

# ? eg:2
##class honda_city:
 #   def engine_specs(self, cc, hp, torque, fuel_type):
 #       print( cc, hp, torque, fuel_type)
 #   def honda_city_body_spaces(self, color, weight, height, length

        
# ! multiple inheritance

# ? it has mltiple parent and 1 child



# ! 
 

# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

# ! heirarical inheritance

##class catagory:
##    def weight(self, weight):
##        print(weight)
##    def display(self, color, taste):
##        print(color, taste)
##class tomato:
##    def tomato_specs(self):
##        color ="black"
##        taste = "neutral taste"
##        self.display
##
##class carrot:
##    def carrot_specs(self):
##        color = "green"
##        taste = "sweet"
##
##c = carrot()
##c.carrot_specs()
##c.weight("30gms")
##


#! hybrid inheritance
# ? the combination of above 4 inheritance is called hybird inheritance


class c1:
    def m1(self):
           print('class1')

class c2(c1):
    def m2(self):
           print('class2')


class c3(c2):
    def m3(self):
           print('class3')

class c4(c2):
    def m4(self):
           print('class4')



class c5(c3):
    def m5(self):
           print('class5')



class c6(c5, c4, c2, c1):
    def m6(self):
           print('class4')

obj = c6()
obj.m3()


# ! ---------> polymorphism

# poly - many, morph ---> form
# A function which has the ability to perform more than 1 functionality then it is considered to be as poliymorphism

# * polymorphism in built functions
# len()---> which is used to find the length of list, tule,dict etc..
# index()
# max()
# count()
# pop()
# and more.....

# * polymorphism in operators

# +
print(8+8)
print("k" +"l")
print([1,2,3]+[5,6])

print(6*7)
l1 = {1,2,3,4,5,6}
print(*l1)
#def f1(*args)
l1 = [1,2,3,4,5]
print(l1*10)

# polymorphism in classes
# we can achieve polymorphism in 2 ways
# 1. method overloading ---> it is not possible in python
# 2. method overriding


















