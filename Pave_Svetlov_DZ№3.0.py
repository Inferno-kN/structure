#Задача 1
struct Animal:
    name: str,
    vid: str,
    age: int,
    ves: float,
    vakcina: bool


#Задача 2
#ключевые сущности: артефакты, дата и члены общества.

struct Artifact:
    materail: str,
    historical_significance: str,
    power: int

struct Data:
    day: int,
    month: int,
    year: int

struct Members_of_the_society:
    role: str,
    clothes: str,
    stage: int,
    artifact: Artifact

#как сущности взаимодействуют.
#перед началом ритуала, члены общества контактируют друг с другом и обсуждают свои артефакты
#до того как члены общества встретились на самом ритуале, они выбрали определенную дату
#как дата была участники встретились, обсудили детали проведения ритуала, показали артефакты друг другу
#в этом ритуале были взаимодействованы все элементы из задания: Члены общества, артефакты и дата проведения ритуала


#Задание 3

#ключ структуры: фермеры, продукты, покупатели и стенды с продуктами

struct Stand:
    massive_products: list[str] ["свежие овощи",
                       "фрукты",
                       "мясные продукты",
                       "молочные продукты"]


struct Farmer:
    name: str,
    age: int


struct Data:
    day: int,
    month: int,
    year: int


struct Products:
    name: str,
    kollvo: int


struct Buyers:
    name: str,
    age: int,
    demograf_character: str,
    product_preferences: list[str],
    money: int


#как характеристики сущностей могут влиять на их взаимодействие и на общую атмосферу рынка, довольно хороший вопрос.
#начну с характеристики фермеров: они могут влиять например опытом продажи и выращивания своей продукции
#покупатели: у каждого покупателя своё кол-во денег и поэтому он будет выбирать товар строго по ценнику и если цена позволяет купить какой либо товар то он возьмет его.
#молодые люди берут чаще всего фрукты, а взрослые пожилые берут овощи или мясо.
#продукты: они могут влиять сроком годности, так как если товар еще годен, то его возможно возьмет какой-нибудь покупатель
#огромное количество разной продукции такие как: свежие овощи, фрукты, мясные и молочные продукты,
# могут привлечь большинство покупателей.








#ЭТО Я ДЛЯ СЕБЯ

class Farmer:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Buyers:
    def __init__(self, name: str, age: int, demograf_character: str, product_preferences: list[str], money: int):
        self.name = name
        self.age = age
        self.demograf_character = demograf_character
        self.product_preferences = product_preferences
        self.money = money

class Product:
    def __init__(self, name: str, kollvo: int):
        self.name = name
        self.kollvo = kollvo

class Data:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

class Stand:
    def __init__(self, massive_products: list[str]):
        self.massive_products = massive_products

class Members_of_the_society:
    def __init__(self, role: str, clothes: str, age: int, artifact: Artifact):
        self.role = role
        self.clothes = clothes
        self.age = age
        self.artifact = artifact

class Artifact:
    def __init__(self, material: str, power: int, historical_significance: str):
        self.material = material
        self.historical_significance = historical_significance
        self.power = power

class Animal:
    def __init__(self, name: str, vid: str, age: int, ves: float, vakcina: bool):
        self.vakcina = vakcina
        self.name = name
        self.vid = vid
        self.age = age
        self.ves = ves

