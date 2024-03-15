# -----> while loop
#----> break using while loop

# Eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
# 2.)
i = 20
while i<31:
    print(i)
    i+=1
    if i==27:
        break
   
# 3.)
i = 20
while i<31:
    print(i)
    if i==27:
        break
    i+=1


# 4.)

i = 20
while i<31:
    if i==27:
        print(i)
        break
    i+=1

#  !  -----> continue
#   ---->
# Eg : 1
# i = 20
# while i<31:
#        if  i ==27:
#               continue
#       print(i)
#       i = i+1

i  =  20
while i < 31:
    i = i+1
    if i==27:
       continue
    print(i)

#  !  Eg : 5
# while to iterate from 12 to 22
#  find the sum of all numbers
# i = 12
# sum=0
# while i<23:
#   sum=sum+i
#    i+=1
# print(sum)

   
 # ! Eg:6
 # Find the average of value from 20 to 25
 #i = 20
 #sum = 0
 #count = 0
 #while i<=30
 #     sum = sum+i
 #     count+=1
 #     i+=1
 #     print(sum/count)
 
 # ! ----> Nested for loop
 # Eg:1

 # for i in range(1, 3+1):
 #    for j in range(1, 4+1):
 #       print(row ,col)

 # Eg:2
 # * * * *
 # * * * *
 # * * * *
 # * * * *

rows = int(input("enter the rows: "))
cols = int(input("enter the cols: "))

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print()


for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()

# ! to print stars in right angled triangle


for row in range(0, 6):
    for col in range(0, row+1):
        print(row, end=" ")
    print()

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for row in range(6, 0, -1):
    for col in range(0, row):
        print(row, end=" ")
    print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *

for row in range(0, 5):
    for col in range (0, 6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *



# ----. datatypes
# primary
#number> int, float, complex;
#string
#boolean
#none

# ----> collection
#list
#tuple
#set
#dictionary


# ? -------> list
# if thecollection of elements ar sourounded by square  brackets,it is considereg to be list
# ! eg:
   # 11 =[4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

# * Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# to acces the elements in list
l1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
# print(l1)

# ---> indexing
 #in the collection datatypes like list, tuple, string, the elements will be alloted
#  with pre-defined unique value called index value

# we have 2 types of indexing
#positive indexing ---> stars with 0 from left hand side
#negative indexing ---> starts with -1 from right hand side

# positive indexing
l1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
#print(l1[0])
#print(l1[4])
#print(l1[20])

# ? negative indexing
l1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
#print(l1[-1])
#print(l1[-5])

# ? -----> slicing
l1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
#l1[start_index:end_index:step]

#print(l1[0:4])
print(l1[6:8])
print(l1[3:6])
print(l1[:5])
print(l1[3:])
print(l1[:])


print(l1[0:7:1]) # l1[0:7] ---> both are same
print(l1[0:7:2])

trail = int(input())
l1 = [1, 4, 1, 89.7, 7.5, "p", "i"]
print(l1[-1:-4])
print(l1[-7:-1:2])


to insert or add element inside list

# append()
l1 =[9, 8, 0, 6]
l1.append("car")
print(l1)





































