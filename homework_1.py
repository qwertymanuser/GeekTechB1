#1 Задача 
int("578") #строка 578 из string превратится в integer
int(673.3123) #строка 673.3123 из float превратится в integer
float(512) #строка 512 из integer превратится в float
int(float(str(192))) #integer
float(173) + 5 #float плюсуется с integer , ответ будет 178.0
str(193.000000000001) #строка 193.000000000001 из float превратится в string

#2 Задача
#Конкатенация - метод, который позволяет объединить несколько строк в одну. Для объединения строк используется знак +
'Calling ' + str(911) #строка Calling и 911 объединились в одну , в итоге вывело "Calling 991"
'abc' + 'xyz' #строка abc и xyz объединились в одну , в итоге вывело "abcxyz"

#3 Задача
a = 589
b = 932.901
c = 'Hello world'
d = '892.01' #можно складывать c и d , получится "Hello World892.01" , также a и b , получится "589932.901"

#4 Задача (Дополнительные)
a = 589
b = 932.901
c = 'Hello world'
d = '892.01'
print(c,a,d,b,a,1481.01)