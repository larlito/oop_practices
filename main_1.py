#1
class Animal:
    def __init__(self,name: str, view: str, age:int,speech: str):
        self.name = name
        self.view = view
        self.age = age
        self.speech = speech

    def print_speech(self):
        print(f'Животное {self.name} издает звук {self.speech}')


    def info_animal(self):
        print(f'Информация о животном')
        print(f'Имя: {self.name}')
        print(f'Вид: {self.view}')
        print(f'Возраст: {self.age}')
        print(f'Звук: {self.speech}')

#2
class Book:
    def __init__(self,name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def open_page(self, number_page: int):
        result = f'Страницы {number_page} не существует'
        if number_page > self.pages:
            result = result
        else:
            result = f'Страница {number_page} открылась'
        return result

    def info_book(self):
        print('Информация о книге:')
        print(f'Название: {self.name}')
        print(f'Автор книги: {self.author}')
        print(f'Кол-во страниц: {self.pages}')


#3
class PassengerPlane:
    def __init__(self,manufacturer: str, model: str, capacity: int, current_height: float, current_speed: float):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def takeoff_plane(self):
        return 'Самолет взлетел!'

    def landing_plane(self):
        return 'Самолет приземлился!'

    def сhange_height(self, new_height: float):
        self.current_height = new_height
        return f'Новая высота {self.current_height}'

    def info_plane(self):
        print(f'Информация о самолете:')
        print(f'Производитель: {self.manufacturer}')
        print(f'Модель: {self.model}')
        print(f'Вместимость: {self.capacity}')
        print(f'Текущая высота: {self.current_height}')
        print(f'Текущая скорость: {self.current_speed}')


class MusicAlbum:
    def __init__(self, artist: str, album_name: str, genre: str, track_list: list):
        self.artist = artist
        self.album_name = album_name
        self.genre = genre
        self.track_list = track_list

    def add_track(self, track_name: str):
        self.track_list.append(track_name)
        print(f'Трек {track_name} добавлен в альбом {self.album_name}')

    def delete_track(self, track_name: str):
        while track_name not in self.track_list:
            track_name = input(f'Данного трека нет в альбом {self.album_name}\nВведите другое название >> ')
        self.track_list.remove((track_name))
        print(f'Трек {track_name} удален из альбома {self.album_name}')

    def play_track(self,track_name: str):
        print(f'Трек {track_name} из альбома {self.album_name} начал играть')

    def info_MusicAlbum(self):
        print('Информация об альбоме:')
        print(f'Певец: {self.artist}')
        print(f'Название альбома: {self.album_name}')
        print(f'Жанр альбома: {self.genre}')
        print(f'Список треков: {','.join(self.track_list)}')



class Program:
    @staticmethod
    def main():
        Cat1 = Animal('Barsik', 'Cat', 33, 'Meeeeeew')

        Cat1.print_speech()
        Cat1.info_animal()



        Book1 = Book('Книга пранков', 'Й.Т.Павлович')

        Book1.open_page()
        Book1.info_book()


        Plane1 = PassengerPlane('Кукурузник', 'В-222', 10,9999999,0)

        Plane1.сhange_height()
        Plane1.takeoff_plane()
        Plane1.landing_plane()
        Plane1.info_plane()



        Diskoteka = MusicAlbum('Nedoprogrammist', 'Python', 'hw_1',['int','float','bool','str','list','dictionary'])
        Diskoteka.add_track()
        Diskoteka.delete_track()
        Diskoteka.play_track()
        Diskoteka.info_MusicAlbum()





