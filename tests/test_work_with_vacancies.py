import pytest
from src.work_with_vacancies import Vacancies


@pytest.fixture
def vacancy():
    return Vacancies('Python', 'https://hh.ru/vacancy/94120582', 60000, 'Казань')


def test_vacancy(vacancy):
    assert vacancy.title == 'Python'
    assert vacancy.url == 'https://hh.ru/vacancy/94120582'
    assert vacancy.salary_from == 60000
    assert vacancy.city == 'Казань'


def test_str(vacancy):
    assert str(vacancy) == ('Название: Python \n'
                            'Город: Казань \n'
                            'Зарплата: 60000 \n'
                            'URL: https://hh.ru/vacancy/94120582\n')
