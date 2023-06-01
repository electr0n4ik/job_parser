import json
import os
from src.abc.abc_job_file import JobFile


class TXTJobFile(JobFile):
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def criteria_matches(vacancy, criteria):
        # Проверяем, соответствует ли зарплата критериям
        if 'salary_min' in criteria and vacancy.get('salary_min') < criteria['salary_min']:
            return False

        # Проверяем, соответствует ли должность критериям
        if 'job_name' in criteria and vacancy.get('job_name') != criteria['job_name']:
            return False
        # TODO
        # Подумать над другими проверками критериев
        # Другие проверки критериев...

        return True

    def add_vacancy_txt(self, vacancy_data):
        os.chdir(os.path.abspath(".."))
        folder_path = os.path.abspath("data_vacancies")
        file_path = os.path.join(folder_path, self.filename)

        with open(file_path, "w") as file:
            file.write(json.dumps(vacancy_data))

    def get_vacancies(self, criteria):
        vacancies = []
        with open(self.filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                for vacancy in data:
                    if self.criteria_matches(vacancy, criteria):
                        vacancies.append(vacancy)
        return vacancies

    def remove_vacancy(self, vacancy_id):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                filtered_data = [vacancy for vacancy in data if vacancy.get('id') != vacancy_id]

        with open(self.filename, 'w') as file:
            file.write(json.dumps(filtered_data))
