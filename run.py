from src.trudvsem import TrudVsem


def process_digits(input_string):
    digits = set(input_string)

    if digits.issubset({'1', '2', '3', '4'}):
        return sorted(digits)
    else:
        return "Запрос/сы выбран/ны неверно"


def user_interface():
    """Функция для взаимодействия с пользователем в консоле."""
    flag_1 = True
    flag_2 = True

    hh = "HeadHunter()"
    sj = "SuperJob()"
    tv = "TrudVsem()"
    list_platforms = [hh, sj, tv]

    search_func = 0
    top_n = 0
    vac_region = 0
    key_word_des = 0
    list_req = [search_func, top_n, vac_region, key_word_des]  # TODO

    print("\n---Парсер вакансий---\n")
    print("Получает информацию о вакансиях с разных платформ:\n1. headhunter.ru\n2. superjob.ru\n3. trudvsem.ru"
          "\n0. Выход\n"
          "\nСохраняет информацию в файл и позволяет удобно работать с ней (добавлять, фильтровать, удалять).")
    while flag_1:
        user_input_pl = input("Выбери цифрой платформу: ")
        if user_input_pl in ["1", "2", "3"]:
            print(f"Выбран сайт {list_platforms[int(user_input_pl) - 1]}")
            while flag_2:
                print("1. Ввести поисковый запрос\n2. Получить топ N вакансий по зарплате;"
                      "\n3. Получить вакансии выбранного региона;"
                      "\n4. Получить вакансии, по ключевому слову в описании.\n")
                user_input_req = input("Выбери цифрой (1, 2, 3, 4) запрос/сы\n(при необходимости несколько): ")
                if process_digits(user_input_req):

                for req in range(len(list_req)):

        elif user_input_pl == "0":
            flag_1 = False
        else:
            print("Платформа выбрана неверно!")


if __name__ == "__main__":
    trudvsem = TrudVsem(2, 10)
    # print(trudvsem.get_vacancies())
    # user_interface()
    user_interface()
