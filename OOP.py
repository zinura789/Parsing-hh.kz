'ООП в Python: https://www.youtube.com/playlist?list=PLQAt0m1f9OHvyjJNjZK_unnLwMOXPTja8'

'''________________ООП 1 Классы, объекты, экземпляры классов._______________'''
isinstance(4, int) #проверка принадлежности классу(типу)
#каждое значение в питоне представляет из себя объект какого-то класса
isinstance(list, object) #сами классы являются объектами
#класс - это шаблон с помощью которого создаются объекты
#в классе мы описываем какие данные будут хранить объекты и какое у них будет поведение

#cоздание класса
class Car:
    pass

Car() #cоздание экземпляра класса
a = Car() #присвоение экземпляра класса переменной

#класс с атрибутами
class Person:
    name = 'Ivan'
    age = 30

'''_____________________ООП 2 Атрибуты класса.______________________________________'''

#действия над атрибутами класса, изменения распространятся на каждый экземпляр класса
Person.name #обращение к атрибуту класса
Person.__dict__ #перечисление всех атрибутов класса

getattr(Person, 'x', 100)# если атрибута 'x' нет, то функция вернет третий аргумент (100 в данном случае)
Person.name = 'Misha' #изменение существующего или присвоение нового атрибута
setattr(Person, 'weight', '70') #изменение существующего или присвоение нового атрибута

del Person.weight #удаление атрибута
delattr(Person, 'age') #удаление атрибута

'''_________________ООП 3 Атрибуты экземпляра класса._______________________________'''

#над атрибутами экземпляра можно производить все те же действия, но изменения распространяться только на один экземпляр
#нельзя у экземпляра удалить атрибуты, которые он получает от класса
#если совпаадет название атрибута у класса и у экземпляра, то обращение идет атрибуту экземпляра

'''_________________ООП 4 Функция как атрибут класса. _______________________________'''

class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print("Let's go")

#обращение к методу класса
Car.drive
getattr(Car, 'drive')

#вызов функции класса
Car.drive()
getattr(Car, 'drive')()

# так как в функции drive мы не передали аргумент self, этот метод экземпляры класса не смогут вызвать

'''_____________________ООП 5 Методы экземпляра. Аргумент self._______________________'''

class Cat:
    def hello(self):
        print('Hello world from kitty')
bob = Cat()

Cat.hello # <function Cat.hello at 0x000001C5C630A5E0>
bob.hello # <bound method Cat.hello of <__main__.Cat object at 0x000001C5C631AE80>>

# Чем отличается метод от функции:
# 1. Метод это та же самая функция, но она объявлена внутри класса
# 2. Метод привязан к конкретному объекту, функция не привязана ее можно отдельно вызывать
# 3. При вызове метода, тот объект с которым он связан будет автоматический проставляться в аргумент метода

class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from kitty', args)

    def show_breed(self):
        print(f'my breed is {self.breed}')
    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')
    def set_value(self, value, age=0):
        self.name = value
        self.age = age

'''___________________ООП 6 Инициализация объекта. Метод init._______________________'''

#Магические методы, методы которые имеют название такого вида: __метод__
# __init__ нам нужен для инициализации объекта (для присвоения экземпляру его собственных значений атрибутов)
# __init__ также называется конструктором класса
class Cat:

    def __init__(self, name, breed = 'pers', age=1, color='white'):
        print('hello new object is ', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
tom = Cat('Tom') #в данном примере при создании экземпляра мы обязательно должны
# передать имя экземпляра, так как оно не определено по умолчанию в __init__

'''____________________ООП 7 Практика "Создание класса и его методов".______________'''
class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.x = 0
        self.y = 0

# тот же класс после применения DRY - don't repeat yourself
class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0,0)


from math import sqrt
class Point:

    list_points = []
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self) #каждый новый экземпляр записываем в лист, который является атрибутом класса

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0,0)

    def print_point(self):
        print(f"Точка с координатами ({self.x},{self.y})")

    def calc_distance(self, another_point): #пример метода, с использованием другого экземпляра класса
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


'''_____________________ООП 8 "Моносостояние"______________________________'''
# если мы хотим чтобы изменение атрибутов одного экземпляра, распространилось
# на все другие экземпляры, то мы можем создать один словарь с атрибутами для всего
# класса и ссылаться на него в конструкторе класса в методе __init__
class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__=Cat.__shared_attr

'''___________ООП 9 Публичные, приватные, защищенные атрибуты и методы_____'''
#Public attr and methods
class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

account1 = BankAccount('Bob', 100000, 4654215645)
#при публичных атрибутах доступ к атрибутам и через метод и через вызов атрибута экземпляра возможен
account1.print_public_data() # Bob 100000 4654215645
print(account1.name) # Bob

#Protected attrs and methods (защищенные атрибуты и методы)
# используем одно нижнее подчеркивание перед переменной, пример: _name
class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)
account1 = BankAccount('Bob', 100000, 4654215645)

#при защищенных атрибутах также как и при публичных атрибутах доступ к атрибутам
# и через метод и через вызов атрибута экземпляра сохраняется, но если мы видим
# защиенные атрибуты и методы это сигнал для программиста не использовать их вне класса
account1.print_protected_data()() # Bob 100000 4654215645
print(account1.name) # Bob

#Private attrs and methods (приватные атрибуты и методы)
# используем два нижних подчеркивания перед переменной, пример: __name
class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)
account1 = BankAccount('Bob', 100000, 4654215645)
#приватные методы и атрибуты возможно использовать только через метод, который дает такой доступ
account1.print_private_data() #Bob 100000 4654215645
print(account1.__name) #AttributeError: 'BankAccount' object has no attribute '__name'
#Инкапсуляция - когда мы даем возможность обратиться к приватным данным, только через метод класса

#на самом деле у нас есть доступ к приватным атрибутам и методам, но не через прямое обращение
#для этого нужно:
# 1. посмотреть какие есть атрибуты у нашего экземпляра через функцию dir
# 2. мы увидим приватные методы и атрибуты в след. виде: _Название класса__название метода
# 3. вызвав их в таком виде мы увидим их значения
print(dir(account1)) # ['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', ...]
print(account1._BankAccount__name) # Bob

#чтобы полностью защитить свои данные нужно использовать модуль accessify внутри которого есть два декоратора protected и private

"""______________________________ООП 10 Геттеры и сеттеры, property атрибуты________________________________"""
#геттеры и сеттеры это методы для доступа к приватным данным
#свойство property дает возможность обращаться экземплярам к приватным данным напрямую
# (так как в своем определении в классе содержит в себе ссылки на геттеры и сеттеры)
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance
    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

"""_______________________ООП Python 11 Декоратор Property _________________________"""

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    @property
    def my_balance(self):
        print('get balance')
        return self.__balance
    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

#геттеры и сеттеры нужно называть одинаково

"""________________ООП 12 Property Вычисляемые свойства___________________"""

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side**2
        return self.__area

'''____________________Практика по методам и свойствам (property)______________________'''

from string import digits
class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def secret(self):
        s = input('Введите ваш пароль: ')
        if s==self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value)<4:
            raise ValueError("Пароль должен быть, больше 4 символов")
        if len(value)>12:
            raise ValueError("Пароль должен быть, меньше 12 символов")
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы 1 цифру")
        self.__password = value

