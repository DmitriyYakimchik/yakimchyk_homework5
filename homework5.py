# Dzmitry Yakimchyk
# Homework-5
# 21-06-2023
# Grodno-IT-Academy-Python 3.11

# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
def get_ranges(input_list: list) -> str:
    """Попаю первый элемент во вспомогательный список пока удовлетворяет условию,
    затем сворачиваю"""
    # Хорошее логичное решение, замечаний нет, для корректировки с join - см ответы
    output = list()
    output_string = ''
    # output_string = list()
    for i in range(len(input_list) + 1):
        if input_list:
            ind = input_list.pop(0)
        if not output or ind == output[-1] + 1:
            output.append(ind)
        elif ind != output[-1] + 1:  # Тут сворачиваю
            if len(output) == 1:
                output_string += str(*output)
            else:
                output_string += f'{output[0]}-{output[-1]}'
            output = [ind]
            output_string += ', '  # очень хотел через join, но получилось только с костылем
    if output_string[-1] == ' ':
        output_string = output_string[:-2]
    return output_string
    # return ', '.join(output_string)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))


# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []
def standardise_phones(*args):
    """Пробую пропарсить значения по-очереди, если хоть одно не является номером,
     то возврат пустого списка. Иначе подгоняю под один формат"""
    import phonenumbers
    from phonenumbers.phonenumberutil import NumberParseException
    # Отличное решение с использованием библиотеки, круто, что обрабатываешь исключение, вместо фильтрации символов, интересно
    solution = []
    for i in args:
        try:
            my_number = phonenumbers.parse(str(i), "BY")
            e164_f = phonenumbers.format_number(my_number, phonenumbers.PhoneNumberFormat.E164)
            solution.append(e164_f)
        # Ошибка при обработке номера
        except NumberParseException:
            print('Not all elements are phone numbers=')
            return list()
    return solution


# Создайте декоратор handle_multiples который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# здесь можно пользоваться циклами
def dec(rope_product):
    def wrapper(*args):
        # Если не делать условных операторов, то будет ошибка при одном параметре,
        # тк там нужен int а возвращается list
        # Да, правильно, тут нужно условие
        if len(args) == 1:
            return rope_product(*args)
        else:
            return [rope_product(arg) for arg in args]
    return wrapper


# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!
# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54
@dec
def rope_product(n: int) -> int:
    """Самые большие результаты умножения двоек и троек.
    Поэтому делаю два набора из доминирующих отрезков (двойки, тройки),
    что больше то и возвращаю"""
    # Ниже оставил решение, которое долго пытался переделать.
    # Там были ошибки для некоторых значений. Например, 7 и 10.
    # Просто удалять было бы жалко)
    # Шикарное решение, замечаний нет. Для альтернативного - см ответы
    if n < 2:
        return n
    first = n // 2
    second, fourth = 0, 0
    if n % 2:
        first = (n - 3) // 2
        second = 1
    third = n // 3
    if n % 3:
        third = (n - 2) // 3
        fourth = 1
    answer_1 = 2 ** first * 3 ** second
    answer_2 = 3 ** third * 2 ** fourth
    return max(answer_1, answer_2)


# def rope_product(n: int) -> int:
#     """Проверяю сколько троек в числе, затем сколько двоек.
#     В ответе складываю их количество"""
    # if n > 4:
    #     if n == 7:
    #         return 12
    #     first = n // 3
    #     second = 0
    #     if n % 3 == 2:
    #         second = (n - first * 3) // 2
    #     answer = 3 ** first * 2 ** second
    #     return answer
    # else:
    #     return n

# for i in range(12):
#     print(rope_product(i), '---', i)
