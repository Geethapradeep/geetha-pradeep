

# ! method riding
# * polymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()


# ! eg:2

class usa:
    def langauge(self):
        print("english")
    def capital(self):
        print("washington dc")
        

class india(usa):
    def langauge(self):
        print("none")
    def capital(self):
        print("new delhi")

i = india()
i.langauge()
i.capital()


# ! eg:3
# ? polymorphism using objects

# c1, c2, ----> c1 = print(c1), print(c2)
# f1, f2

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

obj2 = c1()
obj2.f1()

# ! eg:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)


# changing the functionality of builtin functions

##a = 9
##b = 6
##print(a+b)
##print(a.___add__(b)) # ? dunder method or mafic method

# int()
#print(a.___sub___(b))



##class shopping:
##    def item__list(self, l1):
##        items = len(l1)
##        print(items)
##
##s = shopping()
##print(s)

##class shooping:
##    def ___init___(self, l1):
##        self.items = l1
##        
##    def ___len___(self):
##        length = len(self.items)
##        return length
##    
##s = shooping[1,2,3,4,5]
##print(len(s))
##
##

class  suming:
    def add(self, a, b):
        print(a+b)
#class add(self,a, b, c):
    def add(self, a, b, c):
        print(a+b+c)

s = suming()
#s.add(4, 3)
s.add(4, 5,1)



# ! eg:2

class summing:
    def add(self, a=None, b=None, c=None):
        if a!= None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj = summing()
obj.add(2)
obj.add(3,4)
obj.add(1, 2, 3)



# ! -----> ABSTRACTION

# the process of hiding the implimentation details is abstraction



class shapes():
    #@abstractmethod
    def sides(self):
        print('All shapes have sides except circle')

class triangle(shapes):
    def sides(self):
        print("3 sides")
    def name(self):
        print("Iam traingle")
    def sides(self):
        pass

class square(shapes):
    def square(self):
        print("4 sides")
    def sides(self):
        pass

tr = triangle()
tr.sides()
tr.name()


# ! rules to define abstract class 1

# 1. Abstract class cannot be instantiated
# 2. from abc import ABC, abstractmethod
# 3. subclass the normal class with ABC
# 4. convert the normal method inside the abstract clas to abstract method
# 5. all the child classes have to be subclasssed with abstract class
# 6. the abstract method should be present in the child class



class c1():
    #@abstractmethod
    def m1(self):
        print("this is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("iam child 1")

    def m1(self):
        fail
class2 = c2()
class2.m2()


    
class password():
  def pwd(self):
      pswd = "agpradeep@223"
      return pswd
class login(password):
    def validate(self, name, password):
       
     if super().pwd() ==password:
        print("welcome", name, '!')
        print("login successfull")
     else:
        print('please check the password')
    def pwd(self):
        pass


login = login()
name = input("enter the name: ")
pswd = input("enter the password: ")
login.validate(name, pswd)


# ! encapsulation

class car:
    name ="bmw"

c1 = car()
print(c1.name)
c1.name ='audi'
print(c1.name)


# ? accessing private date outside the class
class c1:
    ___phone = 123456789
    def display(self):
        print(self.___phone)
c = c1()
c.display()


# ? declare private method

# def decor(func):


class class1:
    def __m1(self):
        print("iam private method")
        
    def __init__(self):
        self.__m1()
c= class1()

# ? nested class:
class class1:
    
   class class2:
    
    name = "pradeep"
    
    def display(self):
        print(self.name)

obj = class1()
print(obj.obj1.name)
obj.obj1.display()

        

                    THE  END 

        
