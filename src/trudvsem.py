from requests import *
import json
from src.mixin import Mixin


class TrudVsem(Mixin):

    def __init__(self, offset=1, limit=1, area=1, per_page=1):
        """
        :param offset:
        :param limit:
        :param area:
        :param per_page:
        """
        self.url = "http://opendata.trudvsem.ru/api/v1/vacancies/"
        self.params = {
            "area": area,
            "per_page": per_page,
            "offset": offset,
            "limit": limit
        }

    @staticmethod
    def printj(data_dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))

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

# URL API и параметры запроса
# url = "http://opendata.trudvsem.ru/api/v1/vacancies/"
# params = {
#     "area": 1,  # Код региона
#     "per_page": 10,  # Количество результатов на странице
# }
#
# # Отправка GET-запроса
# response = get(url, params=params)
#
# # Проверка статуса ответа
# if response.status_code == 200:
#     # Получение данных из ответа
#     data = response.json()
#     # Обработка данных...
#     print(data)
# else:
#     print("Ошибка при выполнении запроса:", response.status_code)
