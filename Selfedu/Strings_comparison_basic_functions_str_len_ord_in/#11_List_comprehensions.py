#to add into the list 
A = []
N = 10

for x in range(N):
    A.append(x**2) #!!!!!

print(A)

or
 

N = 10
A = [x**2 for x in range(N)]
print(A)


A = []
N = 10

A = [x**2 for x in range (N) if x%2 == 0]
print(A)



#Алгоритмы обработки элементов списка

# Алгоритм 1 Разбиваем целое положительное число по цифрам

# Шаг 1
432 % 10 = 2

# Шаг 2

43 % 10 = 3
43 // 10 = 4

# Шаг 3

4 % 10 = 4
4 // 10 = 0

#теперь в программе

x = int(input("Enter a whole number: "))
digs = []
while x:
    digs.append(x%10)  # берем последнюю цифру числа
    x = x // 10        # отбрасываем последнюю цифру числа
print(digs)            # если хотим по порядку вместо digs.append(x%10)  ----> digs = [x%10] + digs

#Алгоритм 2 ; Программа меняющая порядок следования элементов в списке на обратный 


# Алгоритм 3 Сортировка методом выбора от самого мин до самого макс

A = [2, 4, 5, 0, 10]
N = len(A)

for x in range (N-1):
    for j in range (i +1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(A)