def process_digits(input_string):
    digits = set(input_string)

    if digits.issubset({"1", "2", "3", "4", "0"}):
        return sorted(digits)
    else:
        return "Запрос/сы выбран/ны неверно"
