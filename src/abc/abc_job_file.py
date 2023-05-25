from abc import ABC, abstractmethod


class JobFile(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy_data):
        """Добавляет информацию о вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Возвращает данные о вакансиях, соответствующих указанным критериям"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        """Удаляет информацию о вакансии из файла по её идентификатору"""
        pass
