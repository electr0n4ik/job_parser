from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class HeadHunter(JSONJobFile, JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой HeadHunter,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    _api_link = "https://api.hh.ru/vacancies"

    def __init__(self):
        filename = "headhunter.json"
        super().__init__(filename)

    def __str__(self):
        return "headhunter.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        area - Код региона (1 - Москва)
        text - Поисковый запрос
        per_page - Количество вакансий на странице
        """

        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            self.add_vacancy(data_dict)
            return data_dict
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_search_vacancies(self, search_data):
        return self.get_vacancies_api(text=search_data)


from src.func.beautiful_table import print_prettytable_hhru

hh = HeadHunter()

print_prettytable_hhru(hh.get_search_vacancies("python"))
# hh.printj(hh.get_search_vacancies("python"))
