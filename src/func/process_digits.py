def process_digits(input_string):
    digits = set(input_string)

    if digits.issubset({'1', '2', '3', '4'}):
        return sorted(digits)
    elif "0" in input_string:
        return False
    else:
        return "Запрос/сы выбран/ны неверно"
