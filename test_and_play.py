# b = (x**2 for x in range(10)) 
# a = list(b)
# length = len(a)

# print(length)

'''
def f():
    for x in range(10):
        yield x
s = f() # сохранили ее состоняие в некой переменной s

#s - является генератором а раз она является генератором мы можем ее выводить при помощи фкнуции next()

print(next(s))
print(next(s))
print(next(s)) # каждый раз вызывая next мы получаем новое значение x 
'''


def get_all_aver(N):
    count = 0
    S = 0
    for i in range(1, N+1):
        count += 1
        S += 1
        yield S/count


it = get_all_aver(10) #создаеи итератор

print(next(it))
print(next(it))
print(next(it))

# def something():
#     yield 1
#     yield 2
#     yield 3
# myiterator = something()

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))