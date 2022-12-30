#1 Задача. Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно превратить кортеж в список и добавить новое значение ‘Tesla’, затем превращаете список обратно в кортеж
# it_company = ('Google', 'Amazon', 'Microsoft')
# lst_it = list(it_company)
# # print(it_company)
# lst_it.append("Tesla")
# # print(it_company)
# it_company = tuple(lst_it)
# print(it_company)

#2 Задача. Из 1 задания попробуйте вывести индекс ‘Amazon’
# it_company = ('Google', 'Amazon', 'Microsoft', 'Tesla')
# print(it_company.index('Amazon'))

#3 Задача.  Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами
# it_company = ('Google', 'Amazon', 'Microsoft', 'Tesla')
# lst_company = list(it_company)
# lst_company[0] = "Apple"
# it_company = tuple(lst_company)
# print(it_company)

#4 Задача. Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft
# it_company = ('Apple', 'Microsoft', 'Amazon' , 'Tesla')
# print(it_company[0:2])

#5 Задача. Есть кортеж text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview') вам нужно посчитать сколько раз встречается
# слово python независимо от регистра

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview')
# print(text_tuple.count("python"))


#6 Задача. Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}. Объедините их в один при помощи встроенных функций языка Python. Подсказка: метод update()
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#7 Задача. Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2, ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения словаря на 5 и вывести в терминал.
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# num = 5
# for key in numbers:
#     num = num * numbers[key]
# print(num)    



#8 Задача. Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] = '34'
# print(student)


#9 Задача. Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = '16'
# print(student)


#10 Задача. Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)


#11 Задача. Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и значение(Западный Анар)
# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)

#12 Задача (Дополнительные) 
# password = input("Введите пороль: ")
# password2 = input("Подтвердите пороль: ")
# if len(password) < 8:
#     print("Короткий пороль!")
# elif "123" in password2 and password:
#     print("Простой пороль!")    
# elif password != password2:
#     print('Различаются!')    
# else:
#     print("OK")    
#     print("Пороль создан")

