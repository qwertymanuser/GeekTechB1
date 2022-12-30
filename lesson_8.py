# def div(num1 : int = 2, num2 : int = 2) -> float:
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Деление на ноль. Учи математику!"
#     except TypeError:
#         return "Пиши целые числа!"
# print(div(10, 5))
# print(div(10, 2))
# print(div(10, 10))
# print(div(10, 0))
# print(div("10" "0"))


# def calc():
#     while True:
#         try:
#             num1 = int(input("Введите первое число: "))
#             operator =(input("+, -, *, /: "))
#             num2 = int(input("Введите второе число: "))
#             if operator == "+":
#                 print(num1 + num2)
#             elif operator == "-":
#                 print(num1-num2)
#             elif operator == "*":
#                 print(num1 * num2)
#             elif operator == "/":
#                 try:
#                     print(num1 / num2)
#                 except ZeroDivisionError:
#                     print("Деление на ноль!")
#             else:
#                 print("Оператор не найден")
#         except ValueError:
#             print("Пиши целые числа!")
# calc()



# try:
#     print(10 / 0)
# except:
#     print("Ошибка")
#     # raise ValueError("Специально вызвали ошибку с raise")
# finally:
#     print("Я всегда буду работать")



# f = open('hello.txt', 'w')
# f.write("GeekTech1")
# f.close()

# r = open('hello.txt', 'r')
# print(r.read())
# r.close()


# import time
# print(time.ctime())


# def save_login_password(login : str, password : str) -> str:
#     password_file = open('login_passwords.txt', 'a+')
#     if login and len(password) >= 8 and ' ' not in password:
#         password_file.write(f"{login}, {password}, {time.ctime()}\n")
#     else:
#         return "Неправильный логин или пороль"
#     password_file.close()
#     return "Логин и пороль сохранен"

# print(save_login_password('geektech', 'geektech2021'))
# print(save_login_password('askhat', 'geekcoin'))
# print(save_login_password('nurbolot', 'geekcoin2'))
# # print(save_login_password('anonimus', '                  '))



# with open('geek.txt', 'a+') as g:
#     g.write("Askhat\n")

# with open('geek.txt', 'r') as r:
#     print(r.read())



import random
import time
# print(random.randint(1, 100))

def generate_random_number():
    return random.randint(1, 10)

def user_contact(name : str, number : str, secret_key : str):
    with open('wins.txt', 'a+', encoding='utf-8') as win:
        win.write(f"Имя: {name}, номер: {number}, ключ: {secret_key} дата: {time.ctime()}\n")

def main():
    random_number = generate_random_number()
    n = 0
    while True:
        user_input = int(input("Введите число: "))
        n += 1
        if random_number == user_input:
            print("Вы выиграли! Введите свои данные для контакта")
            name = input("Введите свое имя: ")
            number = input("Введите свой номер: ")
            secret_key = input("Введите секретное слово для получение приза: ")
            user_contact(name, number, secret_key)
            print("Спасибо, Ваши данные записаны")
            break
        else:
            print(f"Вы не угадали {5 - n} попыток")
            if 5 - n == 0:
                break
main()