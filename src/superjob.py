from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class SuperJob(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии superjob.ru"""

    __API_KEY = "v3.r.127253021.e26c9a2e287fcc53ee2e9b7707c48cbca371f507.9d915df4e26d27b87fa2066897b5442326417a2e"
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        pass
        # filename = "superjob.json"
        # super().__init__(filename)

    def __str__(self):
        return "superjob.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        town - город ("Москва")
        keyword - Поисковый запрос
        count - Количество вакансий для вывода
        """
        params = {}
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }

        for key, value in kwargs.items():
            params[key] = value

        response = get(self._api_link, headers=headers, params=params)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print("Ошибка при выполнении запроса.")
            return []

    def get_search_vacancies(self, search_data):
        return self.get_vacancies_api(keyword=search_data)


sj = SuperJob()
sj.printj(sj.get_vacancies_api())
