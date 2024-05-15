#1
struct Animal:
    Name: str,
    View: str,
    Age: int,
    Weight: int,
    Vacant: bool

#2
struct MagicArtifact:
    Material: str,
    Historical_significance: str,
    Power: int

struct Ritual_date:
    Ritual_day: int,
    Ritual_mouth: int,
    Ritual_year: int

struct Society_member:
    Role: str,
    Wear: str,
    Social_class: int,
    Artifact: str

# Определите ключевые сущности в ритуалах и традициях этого волшебного общества:
Citizen1 = 'Danil'
Citizen2 = 'Ivan'
Citizen3 = 'Anton'

# Опишите детально каждую сущность,учитыва предоставленные характеристики:
Citizen1 = Society_member('Лидер общества,принимает важные решения','Черный мантия',30,'Золотой посох')
Citizen2 = Society_member('Заместитель лидера общества,правая рука лидера','Фиолетовая мантия',25,'Зачарованный посох')
Citizen3 = Society_member('Обычный житель,работает на благо общества','Потертая кожанная мантия',5,'Волшебнаые перчатки')

#Анализируйте,как сущности взаимодействуют друг с другом во время ритуалов

Во время ритуалов 'Danil' не тратит энергию,'Ivan' тратит 1/2 энергии на изучение новой информации,'Anton' тратит всю энергию на изучение нового информации,'Danil' помогает 'Anton' и 'Ivan' благодаря 'Золотой посох'

#3
struct Stand:
    type_product: str

struct Farmer:
    name: str,
    age:int,
    products: list[str]

struct Item:
    name: str,
    count: int,
    manufacturing_data: struct

struct Shopper:
    name: str,
    age: int,
    demographic: str,
    product_preferences: list[str],
    money_amount:int

# Описание для каждой сущности:
farmer = ('Занимается сельским хозяйством,делает зелья,оружия,броню,продает выращенную продукцию)

Shopper = ('Житель города,исследует городской рынок,приобретает товары для обмена с другими жителями')















