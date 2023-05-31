from abc import ABC, abstractmethod
import json


class JobFile(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy_data):
        """Добавляет информацию о вакансии в JSON-файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Возвращает данные о вакансиях, соответствующие указанным критериям"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        """Удаляет информацию о вакансии из файла по её идентификатору"""
        pass

    @staticmethod
    def printj(data_dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами (Для разработки)"""
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))
