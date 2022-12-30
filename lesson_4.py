#Множества set, frozenset
# a = [1, 3, 4, 5]
# b = [3, 4, 5, 6]
# print(list(set(a + b)))

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(numbers)
#print(numbers[0]) #Нельзя в set выводить по индексу
#print(numbers[::-1]) #Set не поддерживает срезы

# names = {"Askhat", "Kurmanbek", "Daniel", "Asylbek"}
# print(names)
# names.add("Nursultan") #Добовляем Nursultan в set множество
# print(names)
# names.remove("Askhat") #Удаляем Askhat из множества
# print(names)
# names.pop() #Удаляем случайное значение
# print(names)
# # names.update("Kurmanbek") #Добовляет Kurmanbek и делит по буквам
# # print(names)
# names.clear() #Очищаем set
# print(names)

# lst = []
# print(type(lst))
# hello = ""
# print(type(hello))
# st = {}
# print(st)


# lst = [10, 4.0, False, "Geek", [1, 2, 3], {1, 2, 3, 3}]
# print(lst)
# st = {1, 1.1, False, "1"}
# numbers = {10, 5, 20, 100, 1, 2, 3}
# print(st)
# print(sorted(numbers))

# frzn = frozenset([1, 2, 3, 4, 5, 6])
# print(frzn)
# frzn.add(10)
# print(frzn)
# frzn.remove(2)
# print(frzn)


# #Tuple - Кортеж
# numbers = (1, 10, 11, 2, 3, 4 , 5, 4)
# print(numbers)
# tup = (1, 1.0, True, "Hello", [1, 2, 3], {1, 2, 3}, (10, 20))
# print(tup)
# print(tup.count("Hello"))
# print(tup.index(1))
# print(tup[2])
# print(tup[0:3])


# cars = ("BMW", "Mersedes", "Ferrari")
# print(cars)
# last_cars = list(cars)
# print(last_cars)
# last_cars.append("Tesla")
# print(last_cars)
# cars = tuple(last_cars)
# print(last_cars)


# tup = (10,)
# print(type(tup))


# st = {}
# print(type(st))

# student = {"student" : "Askhat", "age" : 18} #Создааем список student
# print(student["age"])
# print(len(student)) #Выводим длину словаря student
# print(student["age"]) #По ключу age выводим значение с словаря student 
# student.setdefault('language', 'Python') #Добавляем в словарь новый ключ и значение
# print(student)
# student.pop('age') #Удаляем по ключ age и его значение
# print(student)
# student['language'] = 'JavaScript' #Обновляем по ключу значение 
# print(student)
# student['place_study'] = 'GeekTech' #Если нужного ключа нет то он добавит его 
# print(student)
# print(student.keys()) #С помощью метода keys получаем все ключи словаря student
# print(student.values()) #С помощью метода values получаем все значения словаря student


contact = {'Askhat' : "0778909091"}
while True:
    command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
    if command == "1":
        print(contact)
    elif command == "2":
        add_name = input("Введите имя: ")
        add_number = input("Введите номер: ")
        if add_name not in contact.keys():
            contact.setdefault(add_name, add_number)
            print("Успешно добавлено")
        else:
            print("Такой контакт уже существует")
    elif command == "3":
        delete_contact = input("Кого удалить?: ")
        if delete_contact in contact:
            contact.pop(delete_contact)
            print("Успешно удалено")
        else:
            print("Такого контакта не существует")