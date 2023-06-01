import os

from src.func.process_digits import process_digits
from src.func.prints import print_operations, print_welcome_user_1, print_welcome_user_2
from src.func.prints import print_result_search
from src.headhunter import HeadHunter
from src.superjob import SuperJob
from src.trudvsem import TrudVsem
from src.vacancy import Vacancy


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

                user_input_req = input("Выбери цифрой (1, 2, 3, 4) запрос/сы\n(при необходимости несколько): ")

                if process_digits(user_input_req):
                    for choice in process_digits(user_input_req):

                        if choice == "1":
                            search_query = input("Введите поисковый запрос: ")
                            res = platform().get_search_vacancies(search_query)
                            print(print_result_search(platform, res))
                            input("Нажмите ENTER, чтобы продолжить!")

                        elif choice == "2":
                            n = int(input("Сколько получить вакансий по убыванию зарплаты? "))
                            # Здесь можно вызвать соответствующую функцию для получения топ N вакансий по зарплате

                        elif choice == "3":
                            vac_region = input("Получить вакансии выбранного региона: ")
                            # Здесь можно вызвать соответствующую функцию для получения вакансий в отсортированном виде

                        elif choice == "4":
                            keywords = input("Получить вакансии, по ключевому слову в описании: ")
                            # Здесь можно вызвать соответствующую функцию для поиска
                            # вакансий с указанными ключевыми словами

                        elif choice == "0":
                            flag_2 = False
                            break

        elif user_input_pl == "0":
            flag_1 = False
            print("До свидания!")
        else:
            print("Платформа выбрана неверно!")
