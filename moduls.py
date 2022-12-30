#1 импортировать сам модуль
# import lesson_7
# print(lesson_7.get_time())
# print(lesson_7.hello())

#2 импортировать отдельные определения из модуля
# from lesson_7 import get_time, hello
# print(get_time())
# print(hello())


#3 импортировать все содержимое модуля сразу
# from lesson_7 import *
# print(get_time())
# print(hello())
# print(it)

##################################################################3

from lesson_7 import numbers, chet
def chet_nechet(num : list) -> list:
    for i in num:
        if i % 2 == 0:
            chet.append(i)
    return chet
# print(chet_nechet(numbers))

