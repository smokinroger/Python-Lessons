##Easy
##Task 1

random_list = [1, 2, 4, 0]
new_list = [i**2 for i in random_list]
print(new_list)


##Task 2


fruit_a = ['apple', 'mango', 'orange', 'pineapple', 'pear']
fruit_b = ['mango', 'apple', 'peach', 'pear', 'watermelon']

total = []

for a in fruit_a:
    if a in fruit_b:
        total.append(a)
print(total)

##Task 3

random_num_list = [1, 2, 3, 4, 54, 213, 9, 21, 12, 27, 3432, 993, 999]
result = [val for val in random_num_list if val > 0 and val % 3 == 0 and val % 4 >= 1]
print(result)


##Normal - not completed

##Task 1

name = input('Введите ваше Имя: ')
surname = input('Введите вашу Фамилию: ')


