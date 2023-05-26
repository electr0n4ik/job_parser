from src.trudvsem import TrudVsem


def user_interface():
    """Функция для взаимодействия с пользователем в консоле."""
    flag = True

    hh = "HeadHunter()"
    sj = "SuperJob()"
    tv = "TrudVsem()"
    list_platforms = [hh, sj, tv]
    list_req = []  # TODO
    print("\n---Парсер вакансий---\n")
    print("Получает информацию о вакансиях с разных платформ:\n1. headhunter.ru\n2. superjob.ru\n3. trudvsem.ru\n"
          "\nСохраняет информацию в файл и позволяет удобно работать с ней (добавлять, фильтровать, удалять).")
    while flag:
        user_input_pl = input("Выбери цифрой (1, 2, 3) платформу: ")
        if user_input_pl in ["1", "2", "3"]:
            print(f"Выбран сайт {list_platforms[int(user_input_pl) - 1]}")
            print("1. Ввести поисковый запрос\n2. Получить топ N вакансий по зарплате;"
                  "\n3. Получить вакансии выбранного региона;"
                  "\n4. Получить вакансии, по ключевому слову в описании.\n")
            user_input_req = input("Выбери цифрой (1, 2, 3, 4) запрос: ")
            # TODO
        else:
            print("Платформа выбрана неверно!")


if __name__ == "__main__":
    trudvsem = TrudVsem(2, 10)
    # print(trudvsem.get_vacancies())
    # user_interface()
    user_interface()
