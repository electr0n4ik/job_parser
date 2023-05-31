from abc import ABC, abstractmethod
import json


class JobApi(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_vacancies_api(self):
        """Подключение к API и получение вакансий"""
        pass

    @staticmethod
    def printj(data_dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))
