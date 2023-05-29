from prettytable import PrettyTable
import json


class Mixin:
    """Красивый вывод информации о вакансии."""
    @staticmethod
    def print_pt(data):
        data_dict = json.loads(data)
        table = PrettyTable()
        table.field_names = table.field_names = ["ID", "Источник", "Регион", "Работодатель",
                                                 "Зарплата", "Должность", "График работы"]

        vacancies = data_dict["results"]["vacancies"]
        for vacancy in vacancies:
            vacancy_data = vacancy["vacancy"]
            vacancy_id = vacancy_data["id"]
            source = vacancy_data["source"]
            region = vacancy_data["region"]["name"]
            company = vacancy_data["company"]["name"]
            salary = vacancy_data["salary"]
            job_name = vacancy_data["job-name"]
            employment = vacancy_data["employment"]

            # Вывод данных
            print("ID:", vacancy_id)
            print("Источник:", source)
            print("Регион:", region)
            print("Работодатель:", company)
            print("Зарплата:", salary)
            print("Должность:", job_name)
            print("График работы:", employment)
            print()

            table.add_row([vacancy_id, source, region, company, salary, job_name, employment])

        print(table)
