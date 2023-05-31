from requests import *
import json
from src.mixin import Mixin
from src.abc.abc_job_api import JobApi


class TrudVsem(JobApi, Mixin):

    def __init__(self):
        self._api_link = "https://opendata.trudvsem.ru/api/v1/vacancies/"

    def __str__(self):
        return "trudvsem.ru"

    def connect(self):
        """
        Данные передаются постранично, не более 100 записей на странице. За пагинацию отвечают offset и limit.
        :param offset: Смещение
        :param limit: Число элементов
        """
        self.url = "https://opendata.trudvsem.ru/api/v1/vacancies/"
        self.params = {
            "offset": offset,
            "limit": limit
        }

    def get_vacancies(self):
        response = get(self.url, params=self.params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            # self.printj(data_dict)
            self.print_pt(json.dumps(data_dict, indent=2, ensure_ascii=False))
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None
