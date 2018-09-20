# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


## От меня: Я не стал делать два скрипта, сделал с обработкой входного аргумента
import os
import sys
import shutil

dir1 = 'dir_1'
dir2 = 'dir_2'
print(sys.argv)
print(os.access(dir1, os.W_OK))
print(os.getcwd())

if sys.argv[1] == 'c':
    os.mkdir(dir1) if not os.path.exists(dir1) else print(f'Путь {dir1} уже создан')
    os.mkdir(dir2) if not os.path.exists(dir2) else print(f'Путь {dir2} уже создан')
    print(f'Пути {dir1} и {dir2} созданы или уже существуют в каталоге {os.getcwd()}')
elif sys.argv[1] == 'd':
    os.rmdir(dir1) if os.path.exists(dir1) else print(f'Путь {dir1} не существует')
    os.rmdir(dir2) if os.path.exists(dir2) else print(f'Путь {dir2} не существует')
    print(f'Пути {dir1} и {dir2} удалены или не существуют в каталоге {os.getcwd()}')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
listdir =[x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
for res in listdir:
    print(str(listdir.index(res))+'. '+str(res)+'\n')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
script_path = os.path.abspath(__file__)
shutil.copy(script_path, os.getcwd()+'\scriptLesCopy.py')

