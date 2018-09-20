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


def dir_remove_create(path, mode='c'):
    result = {'result': 'text', 'error': ''}
    try:
        if mode == 'c':
            os.mkdir(path) if not os.path.exists(path) else print(f'Путь {dir1} уже создан')
            result['result'] = 'Directory created'
        elif mode == 'd':
            os.rmdir(dir1) if os.path.exists(dir1) else print(f'Путь {dir1} не существует')
            result['result'] = 'Directory deleted'
    except Exception as e:
        result['result'] = 'Deletion error' if mode == 'd' else result['result'] = 'Create error'
        result['error'] = str(e)

    return result


    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
def print_curr_dir_list():
    listdir = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
    for res in listdir:
        print(str(listdir.index(res)) + '. ' + str(res) + '\n')

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    script_path = os.path.abspath(__file__)
    shutil.copy(script_path, os.getcwd() + '\scriptLesCopy.py')
