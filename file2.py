

Day 2

#a,b,c = 9,8,7
#print(a,b,c)

#a, b=c=7, 8
#prin(a)
#print(b)
#print(c)
 
#a=b, c = 4, 2
#print(a, b, c)

#---->  swapping variable
a = 7
b = 5

eg:1

temp=a
a=b
b=temp
print(a,b)
#a=5, b=7
print(a,b)

eg:2
a=5
b=7
a=a+b
b=a-b
a=a-b
print(a,b)

a=a*b
b=a/b
a=a/b
print(int(a), int(b))

id() --> used to find the memory address of the variables
a = 7
b = 8
print(id(a))
print(id(b))

# !--> literals
literal is the constant value assigned to a variable
a variable is considers to be constant when it is defines in caps

a= 78 # a is variable

A=78 # Ais constant

hash(--> it creates a hash value for constrant datatypes and provides error for non constant data types
n1 = 89+7j
print(hash(n1))


f1 = [7, 8, 9]
print(hash(f1)) # error --> list is non-constant or multiable datatypes
     
a = 9
b = 90


# ! ---> operators
# ? Operators are symbols which is used to perform various oprations betwee 2 0r more operands
 arithmatic
 assignment
 logical
 relational or comprison
 bitwise
 identity
 membership

 # todo ---> arithmatic --> +, -, *, /, %, //, **
 eg 1
     a = 8
     b = 6
     c = 9
     print(a+b+c)
      input () ---> used to get the runtime input
     n1 = input ("enter the value")
     print(n1)

# ! // --> floor devision
     a = 765433
     b = 19
     print(a//b) #-> the out put will be inn integer & the output will be based on floor value


     # ! **--> used for power of anumber
      print(2**4) # -->

     # ! assignment --> +-=, -=, /=, *=, //=, **=, &=, |=

     a=8
     a+=2
     print(a)

     a = 30
     a-=5
     print(a)

    # ! comparison --> ==, >, <, !=,  >=, <=
     a = 8
     b = 7
     print(a>b)

     a = 9
     b = 5
     print(a==b)
 # ! bitwise operator --> &,|,^, ~, <<, >>
     a = 7
     b = 4
     print(a&b)

 # 2^4 2^3 2^2 2^1 2^0

   8    4    2    1

   0    1    1    1   # --> 7

   0    1   0      0   # --> 4 &

   ---------------------

    0    1   0     0

 256 128 64 32 16 8 4 2 1

 0 0 0 0 0 0 0 0 1 0 0

# ~ --->
      a = 9876
     print(~a)

     a = 9

     # 128 64 32 16 8 4 2 1
     # 0  0 0 0 1 0  0 1 # --> 9

     # 1  1 1 1 1 0 1 1 0 # --> -9

      1 1 1  1 1 1 1 0 1-> 1s compliment of 10
                       1 -> 2s compliment

     # 256 128 64 32 16  8 4 2 1
      # 107

# <<, >>
       print(5>>3)

# ! logical ---> used to compare the expressions
     and, or, not

    a = 6
     print(a>3 and a<10)
     print(a>7 or a<30)
     print(not(a>8 and a<10))

 # ! identify operator
     is, is not
     a = 8
     b = 8
     print(a is b)
     print(a==b)

 a = [1, 2, 3]
 b = [1, 2, 3]
 print(a is not b)


 # ! membership operator
     in, not in
     11 = [7, 8, 9, 0, 6, 5]
     num = 55
     print(num in 11)
     print (num not in 11)

    num = 678
     print(8 in num) # error

 # ! conditional statement
     if, elif, else

     eg 1
     --> c syntax
     if (condition){
         statement:
         statement:
          statement:
 python  syntax
     if condition:
         statement:
         statement:
          statement:
     
eg ;1
         a = 6
         if a:
         print("hello")
         
eg:2
         a = 6
         if a>3:
         print("yes")
 else:
     print("no")
     
eg:3
if 7>8:
    print("hello")
    
eg;4
a = 0
a = none
a = flase
a=""
if a:
    print("yes")

else:
    print("n0")

a number is even or odd
 n = int(input("enter the number"))
 if n %2==0:
     print(n, "is even")
 else:
     print(n, "is odd")

name=str(input(" enter the name"))
age=int(input(" enter the age"))
nationality=str(" enter the nationality"))

     
