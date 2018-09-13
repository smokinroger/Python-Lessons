## Раздел Easy
## Задача 1


def round_func(value, digits="0"):
    value = str(float(value))

    intgr = str(value).split(".")[0]
    fract = str(value).split(".")[1]

    result = str()
    rounded = False
    idx = int()

    if 0 < int(digits):

        if len(fract) <= int(digits):
            idx = len(fract) - 1
            if int(fract[idx]) > 5:
                idx -= 1
            else:
                fract = fract[0:idx + 1]
                rounded = True
        else:
            if int(fract[digits]) > 5:
                idx = int(digits) - 1
            else:
                fract = fract[0:int(digits)]
                rounded = True

        while not rounded:

            calc = int(fract[idx]) + 1

            if calc > 9 and idx != 0:
                idx -= 1
            elif calc <= 9 and idx != 0:
                fract = fract[0:idx] + str(calc)
                rounded = True
            elif calc > 9 and idx == 0:
                intgr = str(int(intgr) + 1)
                fract = ""
                rounded = True
            elif calc <= 9 and idx == 0:
                fract = str(int(fract[idx]) + 1)
                rounded = True

        result = intgr + "." + fract
    elif len(fract) > 0 and int(fract[0]) > 5:

        result = str(int(intgr) + 1)

    else:
        result = intgr

    return float(result)


print(round_func(2.486, 1))
print(round_func(2.1234567, 5))
print(round_func(2.1999967, 5))
print(round_func(2.9999967, 5))

print(str(round(2.484, 1)))
print(round(2.1234567, 5))
print(round(2.1999967, 5))
print(round(2.9999967, 5))



## Задача 2

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return "Unlucky ticket"
    else:

        sum1 = 0
        sum2 = 0

        for val in str(ticket_number)[0:3]:
            sum1 += int(val)

        for val in str(ticket_number)[3:6]:
            sum2 += int(val)

        if sum1 == sum2:
            return "Lucky Ticket"
        else:
            return "Unlucky Ticket"


print(lucky_ticket(123456))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


## Уровень Normal
## Задача 1


def fibonacci_seq(fromv = 0, tov = 3):

    seq_fibonacci = [1, 1]
    idx = 2
    if int(tov) < idx and tov < fromv:
        tov = 3
        fromv = 0

    while idx <= int(tov):
        seq_fibonacci.append(seq_fibonacci[idx - 1] + seq_fibonacci[idx - 2])
        idx += 1

    result = list(seq_fibonacci[fromv:tov])

    return result

print(fibonacci_seq(0,11))
print(fibonacci_seq())
print(fibonacci_seq(3, 11))


##Задача 2
def my_sort_to_max(in_list):

    result_list = list()
    srtd = False

    while not srtd:
        cmin = min(in_list)
        result_list.append(cmin)
        in_list.remove(cmin)

        if len(in_list) == 0:
            srtd = True

    return result_list


print(my_sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

## Задача 3

def filtr (func,itr):
    result_list = list()
    for elmnt in itr:
        if func(elmnt):
            result_list.append(elmnt)
    return result_list


def tstf(x):
    result = False

    if x > 18:
        result = True


    return result


print(filtr(tstf, [1, 2, 3, 4, 5, 20, 34, 42, 51, 19]))


## Задача 4


def isparalvertex(point1, point2, point3, point4):
    if abs(point1[0] - point2[0]) == abs(point3[0] - point4[0]) \
            and ((point1[1] == point4[1]) and (point2[1] == point3[1])):
        return "Точки являются вершинами параллелограмма"
    else:
        return "Точки не являются вершинами параллелограмма"


print(isparalvertex((1, 1), (1, 4), (4, 4), (4, 1)))


