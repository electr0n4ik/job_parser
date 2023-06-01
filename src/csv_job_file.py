import csv
import os
from src.abc.abc_job_file import JobFile


class CSVJobFile(JobFile):
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def criteria_matches(vacancy, criteria):
        # Проверяем, соответствует ли зарплата критериям
        if 'salary_min' in criteria and int(vacancy['salary_min']) < criteria['salary_min']:
            return False

        # Проверяем, соответствует ли должность критериям
        if 'job_name' in criteria and vacancy['job_name'] != criteria['job_name']:
            return False
        # TODO
        # Подумать над другими проверками критериев
        # Другие проверки критериев...

        return True

    def add_vacancy_csv(self, vacancy_data):
        os.chdir(os.path.abspath(".."))
        folder_path = os.path.abspath("data_vacancies")
        file_path = os.path.join(folder_path, self.filename)

        with open(file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=vacancy_data.keys())
            writer.writerow(vacancy_data)

    def get_vacancies(self, criteria):
        vacancies = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if self.criteria_matches(row, criteria):
                    vacancies.append(row)
        return vacancies

    def remove_vacancy(self, vacancy_id):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        with open(self.filename, 'w', newline='') as file:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                if row.get('id') != vacancy_id:
                    writer.writerow(row)
