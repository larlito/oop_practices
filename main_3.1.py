from __future__ import annotations
class Wizard:
    def __init__(self,name: str, faculty: str, level: int, list_spells: list,student_status: bool):
        self.__name = name
        self.__faculty = faculty
        self.__level = level
        self.__list_spells = list_spells
        self.__student_status = student_status

    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty

    def get_level(self):
        return self.__level

    def get_spells(self):
        return self.__list_spells

    def get_status(self):
        return self.__student_status

    def set_faculty(self,new_faculty: str):
        if not isinstance(new_faculty,str):raise TypeError('Введено неправильное значение!')
        self.__faculty = new_faculty

    def set_level(self,new_level: int):
        if not isinstance(new_level,int): raise TypeError('Введено неправильное значение!')
        if new_level >= 0:
            self.__level = new_level


    def set_status(self,new_status: bool):
        if not isinstance(new_status,bool):raise TypeError('Введено неправильное значение!')
        self.__student_status = new_status


    def add_spell(self,new_spell: Spell):
        if not isinstance(new_spell,Spell):raise TypeError('Введено неправильное зеначение!')
        self.__list_spells.append(new_spell)

    def remove_spell(self,del_spell:Spell):
        if not isinstance(del_spell,Spell): raise TypeError('Введено неправильное значение!')
        self.__list_spells.remove(del_spell)

    def increase_magic_level(self,amount: int):
        if not isinstance(amount,int): raise TypeError('Введено неправильное значение!')
        if amount >= 0:
            self.__level += amount

    def __str__(self):
        return (f'Имя волшебника:{self.__name}'
                f'Факультет: {self.__faculty}'
                f'Уровень магической силы:{self.__level}'
                f'Заклинания:{self.__list_spells}'
                f'Статус:{self.__student_status}')

    class Spell:
        def __init__(self,spell_name: str,dificulty_level: int,spell_type: str, spell_info: str):
            self.__spell_name = spell_name
            self.__dificulty_level = dificulty_level
            self.__spell_type = spell_type
            self.__spell_info = spell_info


        def get_spell_name(self):
            return self.__spell_name

        def get_dificulty_level(self):
            return self.__dificulty_level

        def get_spell_type(self):
            return self.__spell_type

        def get_spell_info(self):
            return self.__spell_info

        def set_name(self,new_name: str):
            if not isinstance(new_name,str): raise TypeError('Введено неправильное значение!')
            self.__spell_name = new_name

        def set_dificulty_level(self,new_dificult: int):
            if not isinstance(new_dificult,int):raise TypeError('Введено неправильное значение!')
            self.__dificulty_level = new_dificult

        def set_spell_type(self,new_spell_type: str):
            if not isinstance(new_spell_type, str):raise TypeError('Введено неправильное значение!')
            self.__spell_type = new_spell_type

        def set_spell_info(self,new_spell_info: str):
            if not isinstance(new_spell_info, str):raise TypeError('Введено неправильное значение!')
            self.__spell_info = new_spell_info



        def __str__(self):
            return (f'Название заклинания: {self.__spell_name}'
                    f'Уровень сложности: {self.__dificulty_level}'
                    f'Тип заклинания: {self.__spell_type}'
                    f'Информация о заклинании: {self.__spell_info}')


class Employee:
    def __init__(self,
                 name: str,
                 position: str,
                 departament: str,
                 salary: float,
                 experience: int,
                 completed_works: list):

        self.__name = name
        self.__position = position
        self.__departament = departament
        self.__salary = salary
        self.__experience = experience
        self.__completed_works = completed_works



    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_departament(self):
        return self.__departament

    def get_salary(self):
        return self.__salary

    def get_experience(self):
        return self.__experience

    def get_completed_works(self):
        return self.__completed_works

    def set_name(self,new_name: str):
        if not isinstance(new_name,str):raise TypeError('Введено неправильное значение!')
        self.__name = new_name


    def set_position(self,new_position: str):
        if not isinstance(new_position,str): raise TypeError('Введено неправильное значение!')
        self.__position = new_position

    def set_departament(self,new_departament: str):
        if not isinstance(new_departament,str): raise TypeError('Введено неправильное значение!')

        self.__departament = new_departament

    def set_salary(self,new_salary: float):
        if not isinstance(new_salary,float):raise TypeError('Введено неправильное значение!')
        self.__salary = new_salary

    def set_experience(self,new_experience: int):
        if not isinstance(new_experience,int): raise TypeError('Введене неправильное значение!')
        self.__experience = new_experience

    def set_completed_works(self,new_completed_works: list):
        if not isinstance(new_completed_works,list): raise TypeError('Введено неправильное значение!')
        self.__completed_works = new_completed_works

    def add_project(self,new_project):
        self.__completed_works.append(new_project)

    def delete_project(self, del_project):
        self.__completed_works.remove(del_project)

    def increase_salary(self,salary_addition: float):
        if not isinstance(salary_addition,float): raise TypeError('Введено неправильное значение!')
        self.__salary += salary_addition


class Robot:
    def __init__(self, serial_number: int ,model: str, task: str, battery_level: float, status: bool):
        self.__serial_number = serial_number
        self.__model = model
        self.__task = task
        self.__battery_level = battery_level
        self.__status = status

    def get_serial_number(self):
        return self.__serial_number

    def get_model(self):
        return self.__model

    def get_task(self):
        return self.__task

    def get_battery_level(self):
        return self.__battery_level

    def get_status(self):
        return self.__status

    def set_serial_number(self, new_serial_number: str):
        if not isinstance(new_serial_number, str): raise TypeError('Введено неправильное значение!')
        self.__serial_number = new_serial_number

    def set_model(self, new_model: str):
        if not isinstance(new_model, str): raise TypeError('Введено неправильное значение!')
        self.__model = new_model

    def set_task(self, new_task: str):
        if not isinstance(new_task, str): raise TypeError('Введено неправильное значение!')

        self.__task = new_task

    def set_battery_level(self, new_battery_level: float):
        if not isinstance(new_battery_level, float): raise TypeError('Введено неправильное значение!')
        self.__battery_level = new_battery_level

    def set_status(self, new_status: bool):
        if not isinstance(new_status, bool):raise TypeError('Введене неправильное значение!')
        self.__status = new_status



    def turnon(self):
        self.__status = True

    def turnoff(self):
        self.__status = False

    def __str__(self):
         return     (f'Серийный номер: {self.__serial_number}'
                    f'Модель: {self.__model}'
                    f'Текущая задача: {self.__task}'
                    f'Уровень заряда батареи: {self.__battery_level}%'
                    f'Состояние: {self.__status}')



class Athlete:

    def __init__(self, name: str, age: int, sport: str, achievements: list, status: bool):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__status = status

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport(self):
        return self.__sport

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def set_name(self, name: str):
        if not isinstance(name, str): raise TypeError('Не подходящий тип данных.')
        self.__name = name

    def set_age(self, age: int):
        if not isinstance(age, int): raise TypeError('Не подходящий тип данных.')
        self.__age = age

    def set_sport(self, sport: str):
        if not isinstance(sport, str): raise TypeError('Не подходящий тип данных.')
        self.__sport = sport

    def set_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Не подходящий тип данных.')
        self.__status = status

    def add_achievement(self, achievement):
        if not isinstance(achievement, Achievement): raise TypeError('Не подходящий тип данных.')

        self.__achievements.append(achievement)


    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Возраст: {self.__age}\n'
                f'Вид спорта: {self.__sport}\n'
                f'Достижения: {self.get_achievements()}\n'
                f'Статус: {self.__status}')



class Achievement:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name






















































































































































