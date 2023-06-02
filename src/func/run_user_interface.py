from src.func.prints import print_operations, print_welcome_user_1, print_welcome_user_2
from src.func.prints import print_result_search
from src.headhunter import HeadHunter
from src.superjob import SuperJob
from src.trudvsem import TrudVsem


def run_user_interface():
    """Функция для взаимодействия с пользователем в консоли."""
    flag_1 = True
    flag_2 = True

    hh = HeadHunter
    sj = SuperJob
    tv = TrudVsem
    list_platforms = [hh, sj, tv]

    print_welcome_user_1()

    while flag_1:
        print_welcome_user_2()
        user_input_pl = input("Выбери цифрой платформу: ")
        if user_input_pl in ["1", "2", "3"]:
            platform = list_platforms[int(user_input_pl) - 1]
            print(f"Выбран сайт {platform()}\n")

            while flag_2:
                print_operations()

                choice = input("Выбери цифрой (1, 2, 3, 4) запрос: ")

                if choice == "1":
                    search_query = input("Введите поисковый запрос: ")
                    res = platform().get_search_vacancies(search_query)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")

                elif choice == "2":
                    search_query = input("Введите поисковый запрос: ")
                    n_salary = int(input("Сколько получить вакансий по возрастанию зарплаты? "))
                    if 0 < int(n) < 100:
                        res = platform().get_search_vacancies(search_query, n_salary)
                    elif int(n) < 0:
                        res = platform().get_search_vacancies(search_query, 10)
                    else:
                        res = platform().get_search_vacancies(search_query, 100)
                    print(print_result_search(platform, res, "Зарплата"))
                    input("Нажмите ENTER, чтобы продолжить!")

                elif choice == "3":
                    region = input("Получить вакансии выбранного региона: ")
                    res = platform().get_region_vacancies(region)
                    print(print_result_search(platform, res))
                    input("Нажмите ENTER, чтобы продолжить!")

                elif choice == "4":
                    keywords = input("Получить вакансии, по ключевому слову в описании: ")
                    # Здесь можно вызвать соответствующую функцию для поиска
                    # вакансий с указанными ключевыми словами

                elif choice == "0":
                    flag_2 = False
                    break
                else:
                    print("\nВЫБЕРИ ЗАПРОС ВЕРНО!\n")
                    continue

        elif user_input_pl == "0":
            flag_1 = False
            print("До свидания!")
        else:
            print("Платформа выбрана неверно!")
