import json
from base_saver import BaseSaver


class JSONSaver(BaseSaver):
    """
    Класс для сохранения вакансий в json файл
    """

    def add_vacancy(self, vacancies):
        """
        Сохраняет вакансии в json файл
        """
        vacancy_list = []
        for i in vacancies:
            vacancy_list.append({
                'name': i.title,
                'city': i.city,
                'salary': i.salary_from,
                'url': i.url})
        with open('../data/vacancy.json', 'w') as f:
            json.dump(vacancy_list, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        pass
