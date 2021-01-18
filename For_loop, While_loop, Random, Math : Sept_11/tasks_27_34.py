import math
'''Task27
num = float(input("Enter a number with decimail places:"))
result = num * 2 лищняя 
print(result)   
print(num*2)'''


'''Task 28
num = float(input("Enter a number with decimail places:"))
answer = num*2
print(answer)
print(round(answer,2))'''

'''Task 30
num = math.pi
print(round(num,5))
one line: print(round(math.pi,5))'''

'''Task 29
num = int(input("Enter a whole number over 500:"))
square_root = math.sqrt(num)
print(round(square_root,2))'''


'''Task 31
radius = int(input("Enter a radius of circle:"))
area = math.pi * radius ** 2
print(area)'''

'''Task 32
radius = int(input("Enter a radius of cylinder:"))
depth = int(input("Enter a depth of cylinder:"))
area = math.pi * (radius ** 2)
total_volume = area * depth
print(round(total_volume,3))'''

'''Task 33
num_1 = int(input("Enter your first number:"))
num_2 = int(input("Enter your second number:"))
result_1 = num_1 // num_2
result_2 = num_1 % num_2
print(num_1, "divided by", num_2, "is", result_1, "with", result_2, "remaining")'''

print("""
1) Square
2) Triangle
""")

'''Task 34
num_1 = int(input("Enter a number:"))
if num_1 == 1:
    length = int(input("Enter the length of one side:"))
    area = length ** 2
    print("The area of your chose shape is: ",area)
elif num_1 == 2:
    base = int(input("Enter the length of the base of the triangle:"))
    height = int(input("Enter the height of the triangle:"))
    area_t = (base * height) / 2
    print("The area of your chose shape is: ",area_t)
else:
    print("Error, choose 1 or 2")'''


