d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
d2 = d.copy()
d2["list"] = [5,6,7]
print(d)
print(d2)

#для удаления всех записей из словаря
d.clear()

#Для создания копии словаря
d.copy()

#получать значение словаря по ключу
d.get("list")

#удаляет указанный ключ и возвращает его значение
d.pop(3)

#ыполняет удаление произвольной записи из словаря.
d.popitem()

#возвращает коллекцию ключей. 
d.keys()

for x in d.keys(): # ключи

for x in d.values(): #значения 

#возвращает записи в виде кортежей: ключ, значение
for x in d.items():


for key, value in d.items():
    print(key, value)


# Ключи записываются уже без кавычек и после них ставится знак равно вместо двоеточий. В результате, получаем точно такой же словарь. И такой способ задания работает только, если в качестве ключей выступают строки.
d2 = dict(house = "дом", car = "машина",
tree = "дерево", road = "дорога", river = "река")
