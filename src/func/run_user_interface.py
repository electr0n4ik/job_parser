from src.func.prints import print_operations, print_welcome_user_1, print_welcome_user_2
from src.func.prints import print_result_search
from src.headhunter import HeadHunter
from src.superjob import SuperJob
from src.trudvsem import TrudVsem
from src.json_job_file import JSONJobFile


def run_user_interface():
    """Функция для взаимодействия с пользователем в консоли."""
    global res
    flag_1 = True
    flag_2 = True

    hh = HeadHunter
    sj = SuperJob
    tv = TrudVsem
    list_platforms = [hh, sj, tv]

    print_welcome_user_1()
    # Блок получения информации о вакансиях с выбранной платформы в России
    while flag_1:
        print_welcome_user_2()
        user_input_pl = input("Выбери цифрой платформу: ")
        if user_input_pl in ["1", "2", "3"]:
            platform = list_platforms[int(user_input_pl) - 1]
            print(f"Выбран сайт {platform()}\n")

            while True:
                print_operations()

                choice = input("Выбери цифрой (1, 2, 3, 4) запрос: ")

                if choice == "1":
                    search_query = input("Введите поисковый запрос: ")
                    res = platform().get_search_vacancies(search_query)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "2":
                    search_query = input("Введите поисковый запрос: ")
                    n_salary = int(input("Сколько получить вакансий по зарплате? "))
                    if 0 < int(n_salary) < 100:
                        res = platform().get_search_vacancies(search_query, n_salary)
                    elif int(n_salary) < 0:
                        res = platform().get_search_vacancies(search_query, 10)
                    else:
                        res = platform().get_search_vacancies(search_query, 100)
                    print(print_result_search(platform, res, "Зарплата"))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "3":
                    region = input("Получить вакансии выбранного региона: ")
                    n = input("Количество для вывода: ")
                    res = platform().get_region_vacancies(region, n)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "4":
                    keywords = input("Получить вакансии, по ключевому слову в описании: ")
                    n = input("Количество для вывода: ")
                    res = platform().get_region_vacancies(keywords, n)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")
                    break

                elif choice == "0":
                    break
                else:
                    print("\nВЫБЕРИ ЗАПРОС ВЕРНО!\n")
                    continue

            # Блок сохранения информации о вакансиях в файл
            filename = "data_vacancies.json"
            js_file = JSONJobFile(filename)  # JSON
            file_path = js_file.add_vacancy(res)

            # Блок управления вакансиями в файле
            while True:
                user_choice = input("1 - Посмотреть вакансии\n"
                                    "2 - Фильтровать по зарплате\n"
                                    "3 - Удалить вакансии по id\n"
                                    "0 - Назад\n")

                if user_choice == "1":
                    print(js_file.get_vacancies(platform))
                elif user_choice == "2":
                    pass
                elif user_choice == "3":
                    pass
                elif user_choice == "0":
                    break
                input("Нажмите ENTER, чтобы продолжить!")

        elif user_input_pl == "0":
            flag_1 = False
            print("До свидания!")
        else:
            print("Платформа выбрана неверно!")
