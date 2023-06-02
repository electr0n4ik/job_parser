from src.json_job_file import JSONJobFile
from src.csv_job_file import CSVJobFile
from src.txt_job_file import TXTJobFile


def save_file(choice_save_file: str, vacancies_data: dict):
    """Функция для сохранения вакансий в выбранном формате."""
    if choice_save_file == "1":
        filename = "data_vacancies.json"
        js_file = JSONJobFile(filename)  # JSON
        file_path = js_file.add_vacancy(vacancies_data)
        return file_path

    elif choice_save_file == "2":
        filename = "data_vacancies.csv"
        csv_file = CSVJobFile(filename)  # CSV
        file_path = csv_file.add_vacancy(vacancies_data)
        return file_path

    elif choice_save_file == "3":
        filename = "data_vacancies.txt"
        txt_file = TXTJobFile(filename)  # TXT
        file_path = txt_file.add_vacancy(vacancies_data)
        return file_path

    elif choice_save_file == "0":
        pass
