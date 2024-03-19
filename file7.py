
# ----> Assesment
# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d1.update(d2)
print(d1)

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions
set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=2
                break
    if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print("Disjoint")
else:
    print("joint")               


                
# 3.)
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

l3 =[]

#for val in range(len(list1)):
#    ans = list1[val]+list2[val]
 #   l3.append(ans)
#print(l3)

i =0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)

# ! functions
# ? def
# function is a block of code whichn is used to perform a specific functionality
# function can be created using def keyboard

# ? function has 3 parts
# function declaration
# function defanition
# function call

# eg:1
def greet():
    print("Welcome User! !")

greet()

# eg: 2

def adding():
    a = 8
    b = 6
    c = 5
    d = a+b+c
    print(d)
adding()
adding()
#def greeting(name):
 #   print("Welcome",name)
##for val in  range(3):
#    username = input("enter the name")
 #   greeting(username)

# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

def profile(name, age, place):
    print(name, age, place)
