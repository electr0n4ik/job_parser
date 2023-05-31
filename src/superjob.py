from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class SuperJob(JSONJobFile, JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    __API_KEY = "v3.r.127253021.e26c9a2e287fcc53ee2e9b7707c48cbca371f507.9d915df4e26d27b87fa2066897b5442326417a2e"
    _api_link = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        filename = "sj.json"
        super().__init__(filename)

    def __str__(self):
        return "superjob.ru"

    def get_vacancies(self, **kwargs):
        params = {}
        headers = {
            'X-Api-App-Id': self.__API_KEY
        }
        for key, value in kwargs.items():
            params[key] = value
        # params = {
        #     "keyword": "программист",
        #     "town": "Москва",
        #     "count": 10
        # }

        response = get(self._api_link, headers=headers, params=params)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            self.add_vacancy(data_dict)
            return data_dict
        else:
            print("Ошибка при выполнении запроса.")
            return []


sj = SuperJob()
print(sj.get_vacancies(keyword="программист", town="Москва", count=1))
