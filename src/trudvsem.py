from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class TrudVsem(JSONJobFile, JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой TrudVsem,
    и класса, для работы с файлом, содержащем вакансии trudvsem.ru"""

    _api_link = "https://opendata.trudvsem.ru/api/v1/vacancies/"

    def __init__(self):
        filename = "trudvsem.json"
        super().__init__(filename)

    def __str__(self):
        return "trudvsem.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        offset - смещение
        limit - Количество вакансий для вывода
        region - конкретный регион
        text - ключевое слово для поиска по тексту
            (Для поиска по фразе не указывайте никакие дополнительные символы)
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

    def get_search_vacancies(self, search_data, n=10):
        return self.get_vacancies_api(text=search_data, limit=n)

    def get_region_vacancies(self, region):
        return self.get_vacancies_api(region=region)
