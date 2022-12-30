#1 Задача.  Есть обычная функция def hello(x): print(x * x - 10) Превратите данную функцию в lambda функцию
print((lambda x: x * x) (10))

#2 Задача.  Есть список name = [“Kuma”, “Nurtilek”, “Zina”, “Edzen”, “Kuma”, “Aitenur”, “Zina” ] Уберите дубликаты с данного листа с помощью lambda функций
print((lambda x : set(x))(["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina" ]))


#3 Задача.Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Выведите с помощью lambda функции чётные числа с списка
print((list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ))))

#4 Задача. names = [“azat”, “zina”, “kuma”, “anna”, “sas”] Вывести с помощью lambda функции имена палиндромы
print(list(filter(lambda x : (x == "".join(reversed(x))),["azat", "zina", "kuma", "anna", "sas"])))


