from src.abc.abc_job_api import JobApi


class HeadHunter(JobApi):

    def __init__(self):
        self._api_link = "https://api.hh.ru/"

    def __str__(self):
        return "headhunter.ru"

    def connect(self):
        pass

    def get_vacancies(self):
        pass
