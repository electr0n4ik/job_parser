from requests import *
import json
from src.mixin import Mixin


class TrudVsem(Mixin):
    """API «Работа России»"""
    def __init__(self, offset=1, limit=1):
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
