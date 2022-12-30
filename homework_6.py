# 1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
# FYI и т.п.


# def shorter(doct):
#     doct_dict = doct.title().split()
#     for i in range(len(doct_dict)):
#         print(doct_dict[i][0], end='')
# shorter('Кыргызская Республикаnn sdfgh')        

# 2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in
# the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1.

# aji = {}
# def user (ltr):
#     bek_spl = ltr.lower().split(" ")
#     for name in bek_spl :
#         aji[name] = bek_spl.count(name)
# user("Money, money, money, it's, alwyas sunny, in the richem's world") 
# print(aji)       

# 3) Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
   
# def asylbek(word):
#     izogra1 = list(word)
#     izogra2 = set(word)
#     if len(izogra1) == len(izogra2):
#         return True
#     return False
# print(asylbek("asa"))
# 4) Напишите функцию где мы передаем через аргументы число n как целое
# integer, надо вывести целое число в перевернутом виде
# например: n = 27, тогда перевёрнутое n это 72

# def numbers(num):
#     return int(str(num)[::-1])
# print (numbers(27))

# ДОП ЗАДАНИЕ:

# 5) Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
# духе!” Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что”

# def asyl():
#     while True:
#         otvet = input("спроси что не будь: ")
#         if otvet.find("?")>=0:
#             print("конечно")
#         elif otvet.find("!")>=0:
#             print("успокойся")
#         elif otvet == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")          
# asyl()