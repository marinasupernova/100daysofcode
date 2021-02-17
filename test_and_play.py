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


# def get_all_aver(N):
#     count = 0
#     S = 0
#     for i in range(1, N+1):
#         count += 1
#         S += 1
#         yield S/count


# it = get_all_aver(10) #создаеи итератор

# print(next(it))
# print(next(it))
# print(next(it))

# def something():
#     yield 1
#     yield 2
#     yield 3
# myiterator = something()

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))


''' Iterators '''

# a = [1, 2, 3] # это наш итерируемый обьект (коллекция)
# it = iter(a) #из него мы получаем итератор
# print(next(it)) # с помощью функции next мы перебираем элементы коллекции

#на коллекцию а ссылается итератор it и уже через него мы перебираем элементы коллекции
'''
my_tuple = ("apple", "banana", "cherry")
my_iter = iter(my_tuple)


print(next(my_iter))
print(next(my_iter))
print(next(my_iter))'''



# my_str = "banana"

# for x in my_str:
#     print(x)

'''
my_iter = iter(my_str)


print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
'''
'''
class Point:
    x = 1
    y = 1

pt = Point() # создаем экземпляр класса и переменная pt ссылается на этот экземпляр 
print(Point.__name__)

# класс может содержать:
    #  данные (атрибуты)
    #  методы (функции) - имена методов обычно глаголы в то время как имена класса существительные
'''

class Point:
    x = 1;
    y = 1
    def setCoords(self, x, y): #любой метод обьяаленный внутри класса должен иметь параметер self
                                # потом это параметер self будет указывать на соответствующий экземпляр класса
        self.a = x
        self.b = y

pt = Point()
pt.setCoords(5, 10)

# переменные a b принадлежат конкретному экземпляру класса (pt) и никак не связаны с классом Point

# через srlf можно созжавать локальные переменные для конкретного экземпляра класса


__init___(self): - конструктор 
               - данный метод автоматически вызывается когда создается экземпляр класса 
               - для инициализации обьекта(экземпляра класса) , например: задание изначальных параметров для обьекта