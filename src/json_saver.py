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
        if isinstance(vacancies, list):
            for i in vacancies:
                vacancy_list.append({
                    'name': i.title,
                    'city': i.city,
                    'salary': i.salary_from,
                    'url': i.url})
            with open('../data/vacancy.json', 'w') as f:
                json.dump(vacancy_list, f, indent=4, ensure_ascii=False)
        else:
            vacancy_list.append({
                'name': vacancies.title,
                'city': vacancies.city,
                'salary': vacancies.salary_from,
                'url': vacancies.url})
            with open('../data/vacancy.json', 'w') as f:
                json.dump(vacancy_list, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        pass
