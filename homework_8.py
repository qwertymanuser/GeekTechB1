#1 Задача.
# import random
# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# def random_word(language1):
#     random_vybor = random.choice(language1)
#     with open('ran.txt', 'a+') as k:
#         k.write(f"{random_vybor}\n")
# random_word(language)



#2 Задача.
# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""  

# f = open('text.txt', 'w')
# f.write(text)
# f.close()


# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.""" 

# with open('text.txt', 'w') as q:
#     q.write(text)


#3 Задача.
with open('dav.txt','r',)as f,open('li.txt','r')as v,open('wikipedia.txt','a')as k:
    for i in f:
            k.write(i)
    for n in v:
          k.write(n)



        