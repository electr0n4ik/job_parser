import json
import os
from src.abc.abc_job_file import JobFile


class JSONJobFile(JobFile):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy_data):
        os.chdir(os.path.abspath(".."))
        folder_path = os.path.abspath("data_vacancies")
        file_path = os.path.join(folder_path, self.filename)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(vacancy_data, file, indent=2, ensure_ascii=False)
        return file_path

    def get_vacancies(self, **kwargs):
        vacancies = []
        with open(self.filename, 'r') as file:
            for line in file:
                vacancy = json.loads(line)
                # TODO
                # if self.criteria_matches(vacancy, criteria):
                #     vacancies.append(vacancy)
        return vacancies

    def remove_vacancy(self, vacancy_id):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        with open(self.filename, 'w') as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy.get('id') != vacancy_id:
                    file.write(line)
