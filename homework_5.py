# 1 Задача. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована. Подсказка: Используйте функцию range() или enumerate()
# for i in range(5):
#     print(i+1, '0')
num = [0,0,0,0,0]
for i in enumerate(num):
    print(i)
#2 Задача. Нужно заполнить пустой список от 1 до 100. Полученный результат вывести на экран. Подсказка: используйте функцию range() и пустой список
# numbers = []
# for n in range(1, 101):
#     numbers.append(n)
# print(numbers)


#3 Задача. Вывести на экран все чётные значения в диапазоне от 1 до 497. Подсказка: используйте функцию range() и условия
# for i in range(1, 498):
#     if i % 2 == 0:
#         print(i, "четный")
#     else:
#         print(i, "нечетный")


#4 Задача. Суммирование тысячу чисел: создайте список чисел от 1 до 1 000, затем воспользуйтесь функциями min() и max() и убедитесь в том, что список действительно начинается с 1 и заканчивается 1 000. Вызовите функцию sum() и посмотрите, насколько быстро Python сможет просуммировать тысячу чисел

# num = []
# for i in range(1,1001):
#     num.append(i)
# print(num)
# print(min(num))
# print(max(num))
# print(sum(num))


#5 Задача. Заполнить список ста нулями с помощью функции range()
# for i in range(101):
#     print(0)


#6 Задача.
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# a, b = b, a
# print(a)
# print(b)


#7 Задача.
# while True:
#     a = int(input("Введите свой возраст: "))
#     if a >= 18:
#         print("Доступ разрешен")
#     else:
#         print("Извините, пользование данным ресурсом только с 18 лет")