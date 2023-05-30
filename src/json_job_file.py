import json
import os
from src.abc.abc_job_file import JobFile


class JSONJobFile(JobFile):
    def __init__(self, filename):
        self.filename = os.path.abspath(filename)

    @staticmethod
    def criteria_matches(vacancy, criteria):
        # Проверяем, соответствует ли зарплата критериям
        if 'salary_min' in criteria and vacancy.get('salary_min') < criteria['salary_min']:
            return False

        # Проверяем, соответствует ли должность критериям
        if 'job_name' in criteria and vacancy.get('job_name') != criteria['job_name']:
            return False

        # Другие проверки критериев...

        return True

    def add_vacancy(self, vacancy_data):

        with open(self.filename, "w") as file:
            json.dump(vacancy_data, file)

        with open(self.filename, "r") as file:
            return json.load(file)

    def get_vacancies(self, criteria):
        vacancies = []
        with open(self.filename, 'r') as file:
            for line in file:
                vacancy = json.loads(line)
                if self.criteria_matches(vacancy, criteria):
                    vacancies.append(vacancy)
        return vacancies

    def remove_vacancy(self, vacancy_id):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy.get('id') != vacancy_id:
                    file.write(line)


test = JSONJobFile("package.json")
print(test.add_vacancy("test_data"))
