'''
n = 5

n1 = None
n2 = 1.89
n3 = 'ggg'


n4 = "eed"
n5 = "e\'ed"
n6 = "e'ggg'ed"


# print(n6)
# print(type(n))

print(n1,' - ',n2,' - ',n3)

# шаблон F - строки
print(f"{n1}  -  {n2}  -  {n3}")
print("{} - {} - {}".format(n1,n2,n3))
'''

'''
# Ввод данных 
print('введите первое число: ')
a = int(input())
b = int(input('Введите второе число: '))
print(a,b)
print(a," + ",b," = ", a + b)
'''

'''
# Приведение типов
c = 5.89
print(c)
print(type(c))
c = int (c)
print(c)
print(type(c))
'''

"""
# Округление чисел
a = 5.2323
b = 3.8334
print(round(a*b,2))
"""

"""
# Сокращенное присваивание
iter = 2
iter += 3
iter -= 4
iter %= 5
iter **= 5
"""
# % - выводит остаток от деления


# a = 1 > 4
# print (a)       #False
# a = 1 < 4 and 5 > 2
# a = 1 == 2      #False
# a = 1 != 2      #True

# a = "222dd"
# b = "222dd"
# print (a == b)  #True

# a = 1 < 4 < 5 < 10
# print(a)          #True

'''
username = input("Введите имя: ")
if username == "Маша": print("Ура, это же МАША!")
elif username == "Марина": print("Я так ждала вас, Марина!")
elif username == "Ильнар": print("Ильнар - топ!")
else: print("Привет,",username)
'''

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i += 1
# else:
#     print("Пожалуй")
#     print("хватит )")
# print(i)

'''
# Метод флажка
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0 
        flag = False
        print(i)
    elif i > n // 2: #  делитель числа не может превышать введено число, деленое на 2
        print(n)
        flag = False
    i += 1
'''

'''
# Цикл строковой переменной
a = 'qwerty'        
for i in a: 
    print(i)
'''

"""
# Выводим 5 раз 5 звездочек
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line) 
""" 
   

# работа с текстом   
text = "СъЕШЬ еще этих МяГкИх французских булок"
print(len(text)) #позволяет узнать длину строки
print('СъЕШЬ' in text) # ищет фразуз в тексте, выводт Ложь или Правда
print(text.lower()) # нижнйи регистр
print(text.upper()) # верхний регистр
print(text.replace('еще','ЕЩЕ')) # замена
print(text[0]) 
print(text[1])              # тоже самое
print(text[len(text)-1])    # тоже самое
print(text[-1])
print(text[-5])
print(text[:])    # вывод всего текста
print(text[:2])    # первые две буквы
print(text[len(text)-2:])    # последние две буквы
print(text[2:9])    # со 2 по 9 букву
print(text[6:-18]) # с 6 по 20 букву
print(text[0:len(text):6])    # каждую шестую букву
print(text[0:0:6])            # каждую шестую букву
text = text[2:9] + text[-5] + text[:2]
print(text)







