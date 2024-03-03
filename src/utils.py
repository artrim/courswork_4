from get_api_hh import GetApiHH
from work_with_vacancies import Vacancies
from json_saver import JSONSaver


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    city = input("Введите город: ").title().strip()
    salary_range = int(input("Введите минимальную зарплату: "))

    r = GetApiHH()
    hh_vacancies_list = r.get_api(search_query)
    vacancies_list = Vacancies.cast_to_object_list(hh_vacancies_list)

    sort_vacancies = Vacancies.sorted_vacancies_by_salary(vacancies_list)
    filter_by_city = Vacancies.filter_vacancies_by_city(sort_vacancies, city)
    filter_by_salary = Vacancies.filter_vacancies_by_salary(filter_by_city, salary_range)
    filter_by_top_n = Vacancies.get_top_vacancies(filter_by_salary, top_n)
    j = JSONSaver()
    j.add_vacancy(filter_by_top_n)
    Vacancies.print_vacancies(filter_by_top_n, top_n)


if __name__ == "__main__":
    user_interaction()
