import json
import os
from src.abc.abc_job_file import JobFile


class JSONJobFile(JobFile):
    def __init__(self, filename):
        self.filename = filename

        os.chdir(os.path.abspath(".."))
        folder_path = os.path.abspath("job_parser/data_vacancies")
        self.file_path = os.path.join(folder_path, filename)

    def add_vacancy(self, vacancy_data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancy_data, file, indent=2, ensure_ascii=False)
        return self.file_path

    def get_vacancies(self, platform, **kwargs):

        with open(self.file_path, 'r') as file:

            return self.printj(json.load(file))

    def remove_vacancy(self, vacancy_id):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        with open(self.filename, 'w') as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy.get('id') != vacancy_id:
                    file.write(line)
