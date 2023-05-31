from src.abc.abc_job_api import JobApi
from src.json_job_file import JSONJobFile

from requests import *
import json


class HeadHunter(JSONJobFile, JobApi):

    def __init__(self):
        filename = "hhru.json"
        super().__init__(filename)
        self._api_link = "https://api.hh.ru/vacancies"

    def __str__(self):
        return "headhunter.ru"

    def get_vacancies(self, area=1, text="работа", per_page="10"):
        params = {
            "area": area,  # Код региона (1 - Москва)
            "text": text,  # Поисковый запрос
            "per_page": per_page  # Количество вакансий на странице
        }
        response = get(self._api_link, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            self.add_vacancy(data_dict)
            return data_dict
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_vac_search(self):
        pass
