from main import menu
import sys
import os
import shutil
from victory import victory

while True:
    menu()
    answer = input("Действие: ")
    if answer == '1':
        name = input("Имя папки: ")
        if not os.path.exists(name):
            os.mkdir(name)
        else:
            print("Такая папка уже существует")
    elif answer == '2':
        name = input("Имя папки: ")
        os.rmdir(name)
    elif answer == '3':
        name = input("Имя папки/файла: ")
        copy_name = input("Имя папки/файла копии: ")
        shutil.copy(name, copy_name)
    elif answer == '4':
        print(os.listdir())
    elif answer == '5':
        file = []
        for i in os.scandir(): # возвращает записи каталога вместе с информацией об атрибутах файла
            if i.is_dir():# функция, которая возвращает True если текущая запись является каталогом
                file.append(i)
        print(file)
    elif answer == '6':
        file = []
        for i in os.scandir():  # возвращает записи каталога вместе с информацией об атрибутах файла
            if not i.is_dir():  # функция, которая возвращает True если текущая запись является каталогом
                file.append(i)
        print(file)
    elif answer == '7':
        print(sys.platform)
    elif answer == '8':
        print("\n Создатель этой программы - Али Асылбек\n")
    elif answer == '9':
        victory()
    elif answer == '10':
        print("I occasionally deleted this app :d")
    elif answer == '11':
        print(os.getcwd())
        way = input("Куда сменить рабочий дерикторий?: ")
        os.chdir(way)
        print(os.getcwd())
    elif answer == '12':
        break
    a = input("Продолжить?: ")
    if a == 'yes':
        pass
    else:
        break

