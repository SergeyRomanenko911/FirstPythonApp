s = 'This is string'

i = 1
i = 'Somestring'
i = 1

d = 1.5


print(type(s))
print(type(i))
print(type(d))

class Man:
    pass

print(type(Man))

m = Man()

class Man:
    def __init__(self):
        self.age=17
        self.name='Vasya'

m = Man()
print(m.age, m.name)

class Girl:
    def __init__(self):
        self.__age=18
        self.__name='Masha'

g = Girl()

try:
    print(g.age, g.name)
except AttributeError:
    print('Some error!')

print(g._Girl__age)

class Friend:
    def __init__(self):
        self.__age = None
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
    def info(self):
        print(self.__name, self.__age)
    def __str__(self):
        return self.__name + ' ' + str(self.__age)

f = Friend()

f.set_age(20)
f.set_name('Lena')
f.info()

print(f)

class Developer(Friend):
    def __init__(self):
        super()
        self.__lang = None

    def set_lang(self, lang):
        self.__lang = lang

    def get_lang(self):
        return self.__lang

    def __str__(self):
        return super().__str__() + " " + self.__lang

d= Developer()
d.set_lang('JS')
d.set_name('Serhii')
d.set_age(21)

d.info()

print(d.get_lang())
print(d)

class Friend:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
    def info(self):
        print(self.__name, self.__age)
    def __str__(self):
        return self.__name + ' ' + str(self.__age)

def func(*args):
    print(type(args))
    print(args[0],args[1])

func(1,2,3)

l = [2, 6, 6, 'str', Friend(30, "John")]


user = ("Vasya", "Pupkin")
point = {
    "x":6,
    "y":3
}
print(l)
print(user)
print(point)
print(type(l))
print(type(user))
print(type(point))

l.append('Some')

print(l)
print(len(l))

l.reverse()
print(l)
print(user[0])
list_user = list(user)
print(list_user)
print(point['x'], point['y'])

# цикл от 0 до 5

for i in range(0,5):
    print(i)
# Перебор строки
s = 'Hello Python!'

for i in range(0, len(s)):
    print(s[i], end='')

print("\n")

# Перебор строки по символу
for ch in s:
    print(ch, end='')

# Множества
s = set([2, 4, 1])

print(type(s))

# Входит ли 2 во множество
if 2 in s:
    print(True)
else:
    print(False)

print(type(False))

if 1>=1 and 2<=2 or 3==4:
    print(True)

s = "Hello Python!"

if "Hello" in s:
    print(s)

index = 0
while True:
    if index == 10:
        break
    else:
        print(index, end=" ")
        index +=1

print('\n\n\n\n\n')
# Срез
s = 'Hello world!'
print(s[0])
# С 0 по 5
print(s[0:5])
# С 0 по 5 каждый второй
print(s[0:5:2])

# Срез до 8 символа
print(s[:8])

# Срез с 8 символа
print(s[8:])
# Каждый 2 символ
print(s[::2])

# То же самое с list
l = list(range(0,10))
print(l)
# Каждый 2 символ
print(l[:len(l):2])
# Каждый 2 символ второй способ
print(l[::2])

# Последний символ

print(s[-1])
print(s[-1:])

data ={
    'seau':[],
    'id':1,
    'keys':{}
}

# Функция в функции
def func(a, b):
    def sum(a, b):
        return a + b
    print(sum(a,b))
func(4, 5)

functions = [func, func, func]

for f in functions:
    f(2,4)

# Обьявление функции при помощи lamda

sun = lambda a, b: a + b
print(sun(4, 6))
# Тернарные операторы

max = lambda a, b: a if a >= b else b


print(max(7, 3))
print(max(1, 3))
print(max('HHH', "HH"))

# Подключение библиотеки

import new
print(new.my_sum('Hello ', 'Python!'))

print(new.my_sum(4,3))

from math import cos

print(cos(0))

from math import sin as sinus

print(sinus(2))

# Регулярные выражения

import re as RegEx
# Многострочная строка
xml = '''
<a>
    <b>
        <spa n style="">Text</span>
    </b>
    <br/>
    <span>Text</span>
    <b>
        <spa n style="">Text</span>
    </b>
    <im g src='file.png'>
</a
'''

# Получение поломаных тегов
result = RegEx.findall('<\w+ \w+', xml)
print(result)
# Получение полностью поломаных строк
result_2 = RegEx.findall('<\w+ \w+ .*', xml)
print(result_2)

# Исправление перебором еллементов, заменой их на пофикшеные

for s in result:
    xml = xml.replace(s, s.replace(' ', ''))

print(xml)
