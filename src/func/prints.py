from src.func.beautiful_table import print_prettytable_hhru
from src.func.beautiful_table import print_prettytable_sj
from src.func.beautiful_table import print_prettytable_tv


def print_welcome_user_1():
    print("\n---Парсер вакансий---\n"
          "Получает информацию о вакансиях с разных платформ."
          "\nСохраняет информацию в файл и позволяет удобно работать с ней (добавлять, фильтровать, удалять).")


def print_welcome_user_2():
    print("\n1. headhunter.ru\n2. superjob.ru\n3. trudvsem.ru"
          "\n0. Выход\n")


def print_operations():
    print("1. Ввести поисковый запрос;"
          "\n2. Получить топ N вакансий по зарплате;"
          "\n3. Получить вакансии выбранного региона;"
          "\n4. Получить вакансии, по ключевому слову в описании.\n"
          "\n0. Назад.\n")


def print_result_search(platform, res):
    if f"{platform()}" == "headhunter.ru":
        return print_prettytable_hhru(res)
    elif f"{platform()}" == "superjob.ru":
        return print_prettytable_sj(res)
    elif f"{platform()}" == "trudvsem.ru":
        return print_prettytable_tv(res)
