
# ? Take values of length and breadth of a
# ? from user and check if is square or not.

# length = int(input())
# breadth = int(input())
# if length==breadth:
#     print("its a square")
# else:
#     print("its not square")

# ! Eg:4
# Python program to check whether the
# given integer is multiple of both 5 and 7

 # n = int(input("enter the number: "))
 # if n%5==0 and n%7==0:
  #  print("yes")
 #else:
  #  print("no")

# ! Eg:5
# Write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

          #Cost price (in Rs)                  Tax
          #>100000                             15 % + discount 6%
          #>50000 and <= 100000                10%
          #<= 50000                            5%
price = int(input("Enter the price: "))
amount = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    amount=value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("The onroad cost of bike is: ",total)


# if elif
# Eg:1
a = 7
b = 9
c = 30

#if a>b and a>c:
 #   print("A  is greater")
#elif b>a and b>c:
 #   print("B is greater")
#else: c>a and c>b:
    #print("C is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

mark = int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")

# ! Eg:6
# ? Accept the age of 4 people and display the oldest one.

# ! --> short hand if else
# Eg:1
a = 9
b = 60
# if a<b:
#     print("A")
#else:
#    print("B")
#? ---> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else

# print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent
char = input("Enter the char: ")
if char=="a" or char == "e" or char == "i" or char == "o" or char =="u":
     print(" is a vowel")
else:
    print("consonent")

# ? or

str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")


# ! shorthand if else
char = input("Enter the char: ")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")

# ! ----> elif ladder using short hand if else
# Eg:1
# ? Find greatest among 3 variable using short hand if else
a = 8
b = 5
c = 9

print("A is greater")if a>b and a>c else print("B is greater")if b>a and b>c else print("C is greater")


# ! -------> Looping

# looping can be implimented using
# for loop
# while loop

# ----> for loop
#  ? for loop is used for itearation, if we know the number of times the loop have to run
# ? It is used to iterate the iterable eg(string, list, etc...)

# todo --> Syntax for loop

# for syntax in c
# for(i=0;i<10;i++){
#     print("hello");
# }

# ! for syntax in python
# for user defined_variable in range(start, end, step): default  setp value is 1
# statement
# statement
# statement

# ? Eg:1
# To print the value from 1 t 10 using for loop

for i in range(0,10): #(n, n-1)
    print(i)
    print("hello")

# ? Eg:2
for val in range(1, 15, 2):
    print(val)
   
for val in range(1, 15, 3):

# ? Eg:3
# to decrement the value

 for val in range(10,0, -1):
    print(val)

 for val in range(10,0, -2):
    print(val)
   
 for val in range(10,0, 1):
    print(val)# no output
   
# Eg:4
# ! print the output of 7th multipilcation table from 21 to 43
        # --> method:1
for  val in range(1, 10+1):
        print('7','x',val,'=',val*7)
        # --> method:2
        ans="7 x {} = {}"
        print(ans.format(val,val*7))

        # --> Method:3
        print(f"7 x {val}={val*7}")

# ? Eg:5
# break --> used to teerminate the loop

for val in range (1, 10):
    if val ==6:
        break
    print(val)

# ? Eg:6
for val in range (1, 10):
    if val ==6:
        break
    print(val)

# ? eg:7
for val in range (1, 10):
    if val ==6:
        print(val)
        break

# ! continue
# Eg:1
for val in range(1,10):
    if val ==6:
        continue
    print(val)

# ! pratice problems
# ? print the even number between 20 to 40
for val in range (20, 41, 2): 
     print(val)

# ! --------> while loop
while lop is used when we do not know the number of times the loop have to run
to iterate  the non iterable elements while loop is used


# todo syntax

# initialisation
# while condition
#     statement
#     incre or decre

# ! Eg:1
# to iterate number from 1 to 10

i = 0
while i<11:
    print(i)
    i=i+1 # or I+=1

# eg:2
i = 10
while i>0:
    print(i)
    i-=1

for loo practise
write a program to display sum of odd numbers and even
numbers that fall between
12 and 37(including both numbers)


# ! -----> 1-4+9-16+25=15
n = int(input(" enter the number: ")
sum=0
for val in range (1, n+1):
        sq=val*val
        if val %2!=0
          sum=sum+sq
        else:
            sum=sum-sq
            print(sum)













