#1 Задача
password = "qwerty123456"
user_password = input("Password: ")
if password == user_password:
    print("Password is correct. You are welcome")
else:
    print("Password is incorrect. Please, try again")    

# 2 Задача
number = int(input("Температура: "))
if number < -30:
    print("Там так холодно, лучше дома сиди! ")
elif number >= -30 and number <= 0:
    print("Холодновато. Оденься потепелее!")
elif number >= 0 and number <= 15:
    print("Прохладно. Куртку накинь!")    
elif number >= 15 and number <= 30:
    print("Тепло. Иди погуляй в парке!")    
elif number >= 30 and number <= 50:
    print("Ого. Как жарко!")
elif number >50:
    print("Там такая жара, лучше сиди дома!")        
else:
    print("Ошибка!")    

# 3 Задача
text = """Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money"""    
print(text.count("s"))
print(text.count("t"))

# 4 Задача 
name1 = "Aidana"
name2 = "Adilet"
print(name2.join(name1))