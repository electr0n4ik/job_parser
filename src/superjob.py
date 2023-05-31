from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class SuperJob(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    __API_KEY = "v3.r.127253021.e26c9a2e287fcc53ee2e9b7707c48cbca371f507.9d915df4e26d27b87fa2066897b5442326417a2e"

    def __init__(self):
        self._api_link = "https://api.superjob.ru/"

    def __str__(self):
        return "superjob.ru"

    def get_vacancies(self):

        headers = {
            'X-Api-App-Id': self.__API_KEY
        }
        params = {
            "keyword": "программист",
            "town": "Москва",
            "count": 10
        }

        response = get(self._api_link, headers=headers, params=params)
        data = response.json()

        if "objects" in data:
            vacancies = data["objects"]
            for vacancy in vacancies:
                print(f"Название вакансии: {vacancy['profession']}")
                print(f"Зарплата: {vacancy['payment']} {vacancy['currency']}")
                print(f"Ссылка на вакансию: {vacancy['link']}")
                print("-" * 20)
        else:
            print("Ошибка при получении вакансий.")
