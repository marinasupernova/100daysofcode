'''x, y, z = 1, 2, 3
print(id(x))
print(id(y))
print(id(z))'''

'''x = 1
y = 2

x, y = y, x
print(x, y)'''

'''print(1, 2, 3, sep = ",", end = ":")
print(3, 4, 5)'''

'''name = "Marina"
age = 31
print("Name %s, age %d"% (name, age))'''


'''from array import *

nums = array ('i',[45,324,654,45,264])'''

#print(nums)

#for x in nums:
#    print(x)


'''newValue = int(input("Enter number:"))
nums.append(newValue)

nums.reverse()

nums = sorted(nums)

nums.pop()


newArray =array('i' , [])

more = int(input("How many items: "))

for y in range(0, more):
    newValue = int(input("Enter a num:"))
    newArray.append(newValue)

nums.extend(newArray)

print(newArray)'''


'''getRid = int(input("Enter item index: "))
nums.remove(getRid)
print(nums)'''


'''print(nums.count(45))'''


'''Task 088

from array import *


newArray = array ('i' , [])

for i in range (0, 4):
    List5int = int(input("Enter an integer: "))
    newArray.append(List5int)

newArray = sorted(newArray)
newArray.reverse()

print(newArray)

nums.count(num) 

... .count() - counts the times of number in the list

'''


'''Task 089

from array import *

nums = array ('i', [])

import random

for i in range (0, 5):
    num = random.randint(0, 1000)
    nums.append(num)

for i in nums:
    print(i)'''


'''Task 90 why while? 

from array import *

nums = array ('i', [])

for i in range (0, 5):
    num = int(input("Please enter a number between 10 and 20:"))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Outside of the range")

print("Thank you")

for i in nums:
    print(i)'''


'''Task 091

from array import *

nums = array ('i', [1, 2, 3, 4, 3])

for i in nums:
    print(i)

num = int(input("Enter one num from the list: "))

if nums.count(num) == 1:
    print(num, "is in the list once")
else:
    print(num, 'is in the list', nums.count(num), "times")'''


'''Task 092

from array import *

import random

array1 = array ('i', [])
array2 = array ('i', [])



for i in range (0, 3):
    num = int(input("Please enter a number:"))
    array1.append(num)

for i in range (0, 5):
    num = random.randint(1, 1000)
    array2.append(num)

array1.extend(array2)

array1 = sorted(array1)

for i in array1:
    print(i)'''


'''Task 093 Compare with the solution

from array import *

nums = array ('i', [])
nums2 = array ('i', [])

for i in range (0, 5):
    num = int(input("Please enter a number:"))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

selection = int(input("Please choose one of the numbers: "))

if selection in nums:
    nums.remove(selection)
    nums2.append(selection)
else:
    print("Tha is not the value in the array list")


print(nums)
print(nums2)'''


'''Task 094

from array import *

nums = array ('i', [5, 6, 7, 8, 9])

for i in nums:
    print(i)

selection = int(input("plese enter a number from the list: "))

tryagain = True

while tryagain == True:
    if selection in nums:
        print("This is the position", nums.index(selection))
        tryagain = False
    else:
        print("Not in array. Try again")
        selection = int(input("plese enter a number from the list: "))'''


'''Task 095

from array import *
import math

nums = array ('f', [0.25, 0.35, 0.45, 0.55, 0.65])

num = int(input("Please enter a whole number between 2 and 5: "))

tryagain = True

while tryagain == True:
    if num > 2 and num > 5:
        nums / num
        tryagain = False
    else:
        print("Not in array. Try again")
        num = int(input("Please enter a whole number: "))'''

'''
from array import *

nums = array ('i', [5, 6, 7, 8, 9])
selection = int(input("plese enter a number from the list: "))

while selection not in nums:
   print("Not in array. Try again")
   selection = int(input("plese enter a number from the list: "))

print("This is the position", nums.index(selection))
     
  
        
        








